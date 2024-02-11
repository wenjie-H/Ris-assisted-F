import gymnasium as gym
from gymnasium import spaces
import numpy as np


class InvertedPendulumEnv(gym.Env):
    def __init__(self):
        self.gravity = 9.8
        self.masscart = 1.0
        self.masspole = 0.1
        self.total_mass = (self.masspole + self.masscart)
        self.length = 0.5
        self.polemass_length = (self.masspole * self.length)
        self.force_mag = 10.0
        self.tau = 0.02  # seconds between state updates

        # 观测空间：角度和角速度
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(2,))

        # 动作空间：向左推或向右推
        self.action_space = spaces.Discrete(2)

        self.reset()

    def step(self, action):
        force = self.force_mag if action == 1 else -self.force_mag
        costheta = np.cos(self.theta)
        sintheta = np.sin(self.theta)

        temp = (force + self.polemass_length * self.theta_dot ** 2 * sintheta) / self.total_mass
        thetaacc = (self.gravity * sintheta - costheta * temp) / (
                    self.length * (4.0 / 3.0 - self.masspole * costheta ** 2 / self.total_mass))
        xacc = temp - self.polemass_length * thetaacc * costheta / self.total_mass

        # 更新状态
        self.x += self.tau * self.x_dot
        self.x_dot += self.tau * xacc
        self.theta += self.tau * self.theta_dot
        self.theta_dot += self.tau * thetaacc

        done = self.x < -2.4 or self.x > 2.4 or self.theta < -np.pi / 15 or self.theta > np.pi / 15
        reward = 1.0 if not done else 0.0

        return np.array([self.x, self.theta]), reward, done, {}

    def reset(self):
        self.x = 0.0
        self.x_dot = 0.0
        self.theta = 0.0
        self.theta_dot = 0.0
        return np.array([self.x, self.theta])


# 创建环境实例
env = InvertedPendulumEnv()

# 测试环境
observation = env.reset()
for _ in range(1000):
    # env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        observation = env.reset()

env.close()

