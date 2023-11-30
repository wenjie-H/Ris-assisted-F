import gymnasium as gym
import torch
from gymnasium import spaces
import numpy as np


class War2DEnv(gym.Env):
    # 显示可视化内容，我们的环境不需要这个
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):
        self.xth = 0
        self.target_x = 0
        self.target_y = 0
        self.L = 10
        self.action_space = spaces.Discrete(6)
        self.observation_space = spaces\
            .Box(np.array([-self.L, -self.L]), np.array([self.L, self.L]), dtype=np.float32)
        self.state = None

    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))
        x, y = self.state
        if action == 0:
            x = x
            y = y
        if action == 1:
            x = x
            y = y + 1
        if action == 2:
            x = x
            y = y - 1
        if action == 3:
            x = x - 1
            y = y
        if action == 4:
            x = x + 1
            y = y
        if action == 5:
            x = x
            y = y
        self.state = np.array([x, y])
        self.counts += 1

        done = (np.abs(x) + np.abs(y) <= 1) or (np.abs(x) + np.abs(y) >= 2 * self.L + 1)
        done = bool(done)

        if not done:
            reward = -0.1
        else:
            if np.abs(x) + np.abs(y) <= 1:
                reward = 10
            else:
                reward = -50

        return self.state, reward, done, False, {}

    def reset(self, seed=None, options=None):
        self.state = np.ceil(np.random.rand(2) * 2 * self.L) - self.L
        self.counts = 0
        return self.state, {}

    def render(self, mode="human"):
        return None

    def close(self):
        return None


# if __name__ == '__main__':
#     env = War2DEnv()
#     env.reset()
#     env.step(env.action_space.sample())
#     print(env.state)
#     env.step(env.action_space.sample())
#     print(env.state)