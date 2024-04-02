# import os.path
# import time
from Off_Cost_Cal import calculate_off_delay, calculate_linkquality

from environment1 import SnekEnv
from environment_off import OffloadingEnv, State_I
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_checker import check_env


# 指定使用的环境
env = OffloadingEnv()
model = PPO.load("dqn_lunar", env=env)

import numpy as np
env.reset()


# link_quality = np.array(calculate_linkquality(env.nodes, env.BSs))
# obs = State_I(env.nodes, link_quality, np.zeros(45)).encode_state()

# print(obs)
env.state = env.current_state
for i in range(10):
    action, _states = model.predict(env.state, deterministic=False)
    obs, re, d, s, info = env.step(action)
    print(env.state, action)
# 评估训练后的 policy
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10, render=False)
print(f"After training: mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")
