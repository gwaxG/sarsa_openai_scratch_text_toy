from gym.envs.registration import register

register(
    id='cliff-v0',
    entry_point='gym_cliff.envs:CliffEnv',
)

