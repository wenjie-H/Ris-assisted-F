import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2
import random
import time
from collections import deque

SNAKE_LEN_GOAL = 30

class SnekEnv(gym.Env):

    def __init__(self):
        super(SnekEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(2)

        self.L = 20

        self.observation_space = spaces.Box(-self.L, self.L, dtype=np.int32)
        self.state = None
        self.count = 0
        self.last_state = None

    def step(self, action):
        reward = 0.0
        x = self.state[0]
        if action == 0:
            x += 1
        elif action == 1:
            x -= 1
        else:
            print('error')

        self.state = np.array([x])
        self.count += 1

        done = bool((x == 10) or (abs(x) > self.L))


        if self.count > 100:
            print('count over')
            return self.state, -1000, True, False, {}

        if done:
            if x == 10:
                print('sus')
                reward += 10
            else:
                print('fail')
                reward -= 50
        else:

            y = self.last_state[0]
            if abs(10-y) > abs(10-x):
                reward += 0.5
            else:
                reward -= 0.5

        self.last_state = self.state
        return self.state, reward, done, False, {}

    def reset(self, seed=None, options=None):
        self.state = np.array([random.randint(-20, 20)])
        self.last_state = self.state
        self.count = 0
        return self.state, {}



if __name__ == '__main__':
    env = SnekEnv()
    env.reset()
    while True:
        obs, re, d, s, info = env.step(env.action_space.sample())
        print(obs)
        if d:
            break
