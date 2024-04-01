import gymnasium as gym
from gymnasium import spaces
import numpy as np
from Off_Cost_Cal import calculate_off_delay, calculate_linkquality, calculate_delay_state
from EdgeNetwork.CreateMaps import generate_network
import logging
import cv2
import random
import time
from collections import deque

class State_I:
    def __init__(self, node_positions, node_tasks, node_offload_status):
        self.node_positions = node_positions  # 节点位置信息 [(x1, y1), (x2, y2), ...]
        # self.link_quality = link_quality  # 节点间通信链路质量矩阵或二维列表
        self.node_offload_status = node_offload_status  # 节点的卸载状态 [0, 1, ...]
        self.node_tasks = node_tasks
        # self.node_offload_target = node_offload_target  # 卸载到哪个基站 [0, 1, ...]
        # self.base_station_positions = base_station_positions  # 基站位置信息 [(x1, y1), (x2, y2), ...]

    def encode_state(self):
        adjacency_matrix = []
        for i, pos in enumerate(self.node_positions):
            connections = []

            # connections.append((self.link_quality[i], int(self.node_offload_status[i])))
            # for j, quality in enumerate(self.link_quality[i]):
            connections.extend((pos[0], pos[1], self.node_tasks[i], int(self.node_offload_status[i])))
            adjacency_matrix.append(connections)
        return adjacency_matrix


class OffloadingEnv(gym.Env):
    def __init__(self, num_nodes=45, num_BSs=9):
        super(OffloadingEnv, self).__init__()

        # 创造网络
        self.init_network(num_nodes)
        self.num_nodes = num_nodes

        # 观测空间的取值范围
        low = 0  # 最小值
        high = 200  # 最大值

        # 状态空间：每个节点可以是卸载或未卸载，用0和1表示
        self.observation_space = spaces.Box(low=low, high=high, shape=(num_nodes, 4), dtype=np.uint8)

        # logging.info(str(self.observation_space.sample()))

        # 动作空间：每个节点可以选择卸载或保持，用0和1表示
        self.action_space = spaces.MultiBinary(num_nodes)

        self.link_quality = np.array(calculate_linkquality(self.nodes, self.BSs))

        # 当前状态
        self.current_state = State_I(self.nodes, self.tasks, np.zeros(num_nodes)).encode_state()
        # print(State_I(self.nodes, self.link_quality, np.zeros(num_nodes)))
        self.last_state = State_I(self.nodes, self.tasks, np.zeros(num_nodes)).encode_state()

        print('self.current_state', self.current_state)
        # 最大步数
        self.max_steps = 100

        # 当前步数
        self.current_step = 0

    def init_network(self, num_nodes):
        self.network = generate_network(5, 9, 800)
        self.nodes = sorted(self.network[0], key=lambda point: (point[0], point[1]))
        self.tasks = np.full(len(self.nodes), 100)

        # print(len(self.nodes))
        self.BSs = sorted(self.network[1], key=lambda point: (point[0], point[1]))


    def reset(self, seed=None, options=None):
        # 重置环境，返回初始状态

        off_s = []
        for i in range(self.num_nodes):
            off_s.append(random.randint(0, len(self.BSs)))
        self.current_state = State_I(self.nodes, self.tasks, np.array(off_s)).encode_state()
        self.last_state = self.current_state
        self.current_step = 0
        return self.current_state, {}

    def step(self, action):
        # 执行动作，返回新的状态、奖励、是否终止和额外信息


        # logging.info(str(self.current_state) + ',' + str(len(self.current_state)) + ',' + str(len(self.nodes)))
        current_delay = calculate_delay_state(self.current_state, self.BSs, action)
        # last_delay = calculate_off_delay(self.nodes, self.BSs, action)

        # 计算奖励
        reward = -current_delay  # 示例中每步的奖励为卸载的节点数量的负值
        logging.info('reward:' + str(reward))

        # 检查是否达到终止条件
        done = self.current_step >= self.max_steps


        # 更新步数
        self.current_step += 1

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
    env = OffloadingEnv()

    # 重置环境
    state = env.reset()

    # 执行一些动作
    for _ in range(1000):
        action = env.action_space.sample()  # 随机选择动作
        # print(action)
        next_state, reward, done, _ = env.step(action)
        env.render()

        if done:
            print("Episode finished after {} timesteps".format(env.current_step))
            break

