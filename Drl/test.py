# import os.path
# import time

# from environment1 import SnekEnv

from environment_off import OffloadingEnv
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_checker import check_env
import torch
import time
import os
from stable_baselines3.common.vec_env.dummy_vec_env import DummyVecEnv
def make_env():
    def _init():
        env = OffloadingEnv()
        # env = Monitor(env, './logs/')  # 设置日志文件夹
        return env
    return _init

def train():
    num_envs = 1
    envs = [make_env() for _ in range(num_envs)]
    vec_env = DummyVecEnv(envs)
    policy_kwargs = dict(activation_fn=torch.nn.ReLU,
                         net_arch=dict(pi=[64, 64], vf=[64, 64]))
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = PPO(
        policy='MultiInputPolicy',
        env=vec_env,
        n_steps=1024,
        n_epochs=10,
        tensorboard_log='./tensorboard_logs/',
        policy_kwargs=policy_kwargs,
        verbose=1,
        device=device
    )
    print('Start training')
    loca = time.strftime('%Y-%m-%d_%H-%M-%S')
    model_name = 'ppo_simple_' + str(device) + '_' + str(loca)
    ep_len = 1000
    for _ in range(1000):
        model.learn(
            total_timesteps=ep_len,
            tb_log_name='PPO_Simple_' + str(loca),
            reset_num_timesteps=False
        )
        model.save(os.path.join('models', model_name))
    print('Training finished')
    vec_env.close()


train()