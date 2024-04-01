import gymnasium as gym
from gymnasium import spaces
import numpy as np

# 示例状态
state = [([0, 14, 0, 0, 0, 0, 0, 0, 0], 0),
         ([6, 0, 0, 0, 0, 0, 0, 0, 0], 0),
         ([0, 5, 0, 0, 0, 0, 0, 0, 0], 0),
         ([0, 0, 2, 0, 0, 0, 0, 0, 0], 0),
         ([6, 0, 0, 0, 0, 0, 0, 0, 0], 0),
         ([0, 2, 3, 0, 0, 0, 0, 0, 0], 0)]

# 转换为 numpy 数组
state_array = np.array(state)

# 获取状态空间的形状
num_nodes, num_neighbors, _ = state_array.shape

# 定义状态空间
low = np.zeros((num_nodes, num_neighbors, 2))  # 状态空间中所有元素的下界为0
high = np.ones((num_nodes, num_neighbors, 2))  # 状态空间中所有元素的上界为1
state_space = spaces.Box(low, high, dtype=np.float32)

print("State space shape:", state_space.shape)
