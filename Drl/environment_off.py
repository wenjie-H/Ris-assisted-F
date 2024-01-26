import gymnasium as gym
from gymnasium import spaces
import numpy as np
from Off_Cost_Cal import calculate_off_delay
from EdgeNetwork.CreateMaps import generate_network
import logging
import cv2
import random
import time
from collections import deque
# import numpy as np
# import gym
# from gym import spaces

class OffloadingEnvironment(gym.Env):
    def __init__(self, num_nodes=45):
        super(OffloadingEnvironment, self).__init__()

        # 创造网络
        self.init_network(num_nodes)
        self.num_nodes = num_nodes

        # 观测空间的取值范围
        low = 0  # 最小值
        high = 255  # 最大值

        # 状态空间：每个节点可以是卸载或未卸载，用0和1表示
        self.observation_space = spaces.Box(low=low, high=high, shape=(num_nodes, num_nodes), dtype=np.uint8)

        logging.info(str(self.observation_space.sample()))

        # 动作空间：每个节点可以选择卸载或保持，用0和1表示
        self.action_space = spaces.MultiBinary(num_nodes)

        # 当前状态
        self.current_state = np.zeros(num_nodes)
        self.last_state = np.zeros(num_nodes)

        # 最大步数
        self.max_steps = 100

        # 当前步数
        self.current_step = 0

    def init_network(self, num_nodes):
        self.network = generate_network(5, 9, 800)
        self.nodes = self.network[0]
        self.BSs = self.network[1]


    def reset(self, seed=None, options=None):
        # 重置环境，返回初始状态
        off_s = []
        for i in range(self.num_nodes):
            off_s.append(random.randint(0, 1))
        self.current_state = np.array(off_s)
        self.last_state = self.current_state
        self.current_step = 0
        return self.current_state, {}

    def step(self, action):
        # 执行动作，返回新的状态、奖励、是否终止和额外信息


        # 更新当前状态
        self.current_state = action

        # logging.info(str(self.current_state) + ',' + str(len(self.current_state)) + ',' + str(len(self.nodes)))
        current_delay = calculate_off_delay(self.nodes, self.BSs, self.current_state)
        last_delay = calculate_off_delay(self.nodes, self.BSs, self.last_state)

        # 计算奖励
        reward = -np.sum(action)  # 示例中每步的奖励为卸载的节点数量的负值

        # 检查是否达到终止条件
        done = np.all(self.current_state) or self.current_step >= self.max_steps



        # 更新步数
        self.current_step += 1

        if done:
            if np.all(self.current_state):
                print('sus')
                reward += 10
            else:
                print('fail')
                reward -= 50
        else:


            if current_delay < last_delay:
                reward += 0.5
            else:
                reward -= 0.5


        # 记录上一个状态
        self.last_state = self.current_state

        return self.current_state, reward, done, {}

    def render(self):
        pass
        # 可选的渲染方法，用于显示环境状态
        # print(f"Current State: {self.current_state}")



if __name__ == '__main__':
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='w')
    ch = logging.StreamHandler()
    logger = logging.getLogger()
    logger.addHandler(ch)

    # 测试环境

    env = OffloadingEnvironment()

    # 重置环境
    state = env.reset()

    # 执行一些动作
    for _ in range(20):
        action = env.action_space.sample()  # 随机选择动作
        # print(action)
        next_state, reward, done, _ = env.step(action)
        env.render()

        if done:
            print("Episode finished after {} timesteps".format(env.current_step))
            break

