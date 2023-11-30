# import os.path
# import time

from environment1 import SnekEnv
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_checker import check_env


# 指定使用的环境
env = SnekEnv()
# check_env(env)
# 指定使用的模型
# 第一个参数指定网络类型，可选MlpPolicy，CnnPolicy，MultiInputPolicy
# 如果想使用自定义的网络结构，可以在 policy_kwargs 参数中进行定义
# loca = time.strftime('%Y-%m-%d_%H-%M-%S')
# model_name = 'ppo_bgmenv_' + str('move')
# model = PPO('MlpPolicy', env=env, tensorboard_log='./tensorboard_logs/', n_epochs=5, n_steps=10)
#
#
#
# # 训练之前随机的 policy，可以获得的平均 reward 比较低
# mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10, render=False)
# # print(f"Before training: mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")
# model.learn(total_timesteps=100000, reset_num_timesteps=False)
#
# model.save("dqn_lunar")
# # del model  # delete trained model to demonstrate loading
#
# # Load the trained agent
# # NOTE: if you have loading issue, you can pass `print_system_info=True`
# # to compare the system on which the model was trained vs the current one
# # model = DQN.load("dqn_lunar", env=env, print_system_info=True)
model = PPO.load("dqn_lunar", env=env)

import numpy as np
env.reset()

obs = np.array([0])
env.state = obs
for i in range(10):
    action, _states = model.predict(env.state, deterministic=False)
    obs, re, d, s, info = env.step(action)
    print(env.state, action)
# 评估训练后的 policy
mean_reward, std_reward = evaluate_policy(model, env, n_eval_episodes=10, render=False)
print(f"After training: mean_reward:{mean_reward:.2f} +/- {std_reward:.2f}")
