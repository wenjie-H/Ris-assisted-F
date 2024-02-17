


def make_env():
    def _init():
        env = SimpleEnv()
        env = Monitor(env, './logs/')  # 设置日志文件夹
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


def test():
    env = SimpleEnv()
    model = PPO.load('models/ppo_simple_cuda_2024-01-31_21-43-11.zip', env=env)
    obs, info = env.reset()
    for i in range(200):
        action, _states = model.predict(obs, deterministic=False)
        print('第', i, '次观察：', obs)
        obs, rewards, terminated, truncated, info = env.step(action)
        print('第', i, '次动作：', action)
        print('第', i, '次奖励：', rewards)
        # time.sleep(0.03)
    print(env.detection_data)
    print(env.ep_rew)
    env.close()


if __name__ == '__main__':
    train()