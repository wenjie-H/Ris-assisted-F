import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2
import random
import time
from collections import deque

SNAKE_LEN_GOAL = 30

class OffEnv(gym.Env):

    def __init__(self):
        super(OffEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(2)

        self.L = 20

        self.observation_space = spaces.Box((-self.L, -self.L), (self.L, self.L), dtype=np.int32)
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
                reward += 20
            else:
                print('fail')
                reward -= 100
        else:

            y = self.last_state[0]
            if abs(10-y) > abs(10-x):
                reward += 0.1
            else:
                reward -= 0.1

        self.last_state = self.state
        return self.state, reward, done, False, {}

    def reset(self, seed=None, options=None):
        pass


