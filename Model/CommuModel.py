
def vehicle_to_nodes():
    pass


from Parameter import PathLossExponent, LoSGain, Bandwidth, Noisepower, Transmitpower
import math

def calculate_channel_gain(environment, distance):
    if environment == "LoS":
        channel_gain = math.sqrt(1/(distance**2)**(PathLossExponent/2)) * LoSGain
    else:
        channel_gain = math.sqrt(1 / (distance ** 2) ** (PathLossExponent / 2))

    return channel_gain

# Function to calculate transmission rate based on LoS and NLoS parameters



def calculate_transmission_rate(channel_gain):
    # 信道增益考虑路径损耗
    effective_noise_power = Noisepower / channel_gain  # 通过信道增益调整噪声

    # 计算传输速率，信道增益考虑在内
    transmission_rate = Bandwidth * math.log2(1 + (Transmitpower / effective_noise_power))
    return transmission_rate

# 输入已知的值
# bandwidth = 10e6  # 10 MHz的带宽
# transmit_power = 0.1  # 0.1瓦特的传输功率
# noise_power = 1e-9  # 1纳瓦特的噪声功率
distance = 100  # 100米的距离

# 假设的信道增益，实际情况需根据路径损耗模型或具体环境计算得出
# 这里直接指定了一个值，实际情况应该根据实际环境测量或模拟得出
channel_gain = 0.004/10

# 计算传输速率
gain = calculate_channel_gain('NLoS', 200)
print('gain:', gain)

result = calculate_transmission_rate(gain)/1000000
print(f"传输速率为: {result:.2f} mps")


