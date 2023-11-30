import random
from Plot import plot_gps_points
def CreateNodesObstacles(num1: int, num2: int):

    node_set1 = []
    for i in range(num1):
        node_set1.append([random.randint(0, 500), random.randint(0, 500)])

    node_set2 = []
    for i in range(num2):
        node_set2.append([random.randint(100, 400), random.randint(100, 400)])

    plot_gps_points(node_set1, node_set2)
    # pass

def CreateObstacle(num: int):
    node_set = []
    for i in range(num):
        node_set.append([random.randint(100, 400), random.randint(100, 400)])

    # pass


CreateNodesObstacles(100, 10)