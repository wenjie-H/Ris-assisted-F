import numpy as np
def calculate_distance(coord1, coord2):
    """
    计算两个节点之间的欧氏距离
    """
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)


def generate_adjacency_matrix(coords):
    """
    根据节点坐标生成邻接矩阵
    """
    num_nodes = len(coords)
    adjacency_matrix = np.zeros((num_nodes, num_nodes))

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                distance = calculate_distance(coords[i], coords[j])
                adjacency_matrix[i][j] = distance

    return adjacency_matrix

if __name__ == '__main__':

    # 示例节点坐标
    coordinates = [(0, 0), (1, 1), (2, 2), (3, 3)]

    # 生成邻接矩阵
    adj_matrix = generate_adjacency_matrix(coordinates)
    print("Adjacency Matrix:")
    print(adj_matrix)
