import gymnasium as gym
from gymnasium import spaces
import numpy as np

# 定义观测空间的大小
observation_space_size = (40, 40)

# 观测空间的取值范围
low = 0  # 最小值
high = 255  # 最大值

# 使用Box定义观测空间
observation_space = spaces.Box(low=low, high=high, shape=observation_space_size, dtype=np.uint8)

# 生成一个随机观测样本
sample_observation = observation_space.sample()

# 打印观测空间和样本观测
print("Observation Space:", observation_space)
print("Sample Observation:")
print(sample_observation)
