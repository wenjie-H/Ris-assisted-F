import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2
import random
import time
from collections import deque
# import numpy as np
# import gym
# from gym import spaces

class UninstallEnvironment(gym.Env):
    def __init__(self, num_nodes=30):
        super(UninstallEnvironment, self).__init__()

        # 状态空间：每个节点可以是卸载或未卸载，用0和1表示
        self.observation_space = spaces.MultiBinary(num_nodes)

        # 动作空间：每个节点可以选择卸载或保持，用0和1表示
        self.action_space = spaces.MultiBinary(num_nodes)

        # 当前状态
        self.current_state = np.zeros(num_nodes)

        # 最大步数
        self.max_steps = 100

        # 当前步数
        self.current_step = 0

    def reset(self):
        # 重置环境，返回初始状态
        self.current_state = np.zeros(self.observation_space.shape)
        self.current_step = 0
        return self.current_state

    def step(self, action):
        # 执行动作，返回新的状态、奖励、是否终止和额外信息

        # 更新当前状态
        self.current_state = action

        # 计算奖励
        reward = -np.sum(action)  # 示例中每步的奖励为卸载的节点数量的负值

        # 检查是否达到终止条件
        done = np.all(self.current_state) or self.current_step >= self.max_steps

        # 更新步数
        self.current_step += 1

        return self.current_state, reward, done, {}

    def render(self):
        # 可选的渲染方法，用于显示环境状态
        print(f"Current State: {self.current_state}")



if __name__ == '__main__':
    # 测试环境

    env = UninstallEnvironment()

    # 重置环境
    state = env.reset()

    # 执行一些动作
    for _ in range(20):
        action = env.action_space.sample()  # 随机选择动作
        next_state, reward, done, _ = env.step(action)
        env.render()

        if done:
            print("Episode finished after {} timesteps".format(env.current_step))
            break

