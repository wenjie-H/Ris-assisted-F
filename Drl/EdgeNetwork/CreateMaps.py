import random
import matplotlib.pyplot as plt

def generate_uniform_grid(num_rows, num_cols, field_size):
    grid_step = field_size / max(num_rows, num_cols)
    return [(i * grid_step, j * grid_step) for i in range(num_rows) for j in range(num_cols)]

def generate_network(num_nodes_per_station, num_base_stations, field_size):
    # 生成基站均匀分布的位置
    base_stations = generate_uniform_grid(int(num_base_stations**0.5), int(num_base_stations**0.5), field_size)

    # 生成节点，确保每个基站下面的节点数量相同
    nodes = []
    for base_station in base_stations:
        nodes += [(random.uniform(base_station[0], base_station[0] + field_size*2.4/num_base_stations),
                   random.uniform(base_station[1], base_station[1] + field_size*2.4/num_base_stations))
                  for _ in range(num_nodes_per_station)]

    return nodes, base_stations

def plot_network(nodes, base_stations):
    plt.scatter(*zip(*nodes), color='blue', label='Nodes')
    plt.scatter(*zip(*base_stations), color='red', marker='s', label='Base Stations')
    plt.xlabel('X-axis (m)')
    plt.ylabel('Y-axis (m)')
    plt.title('Randomly Distributed Network Nodes and Base Stations')
    plt.legend()
    plt.show()



if __name__ == "__main__":
    num_nodes_per_station = 10
    num_base_stations = 9  # 请确保基站数量为平方数，以便均匀分布在场地上
    field_size = 800

    nodes, base_stations = generate_network(num_nodes_per_station, num_base_stations, field_size)
    plot_network(nodes, base_stations)
