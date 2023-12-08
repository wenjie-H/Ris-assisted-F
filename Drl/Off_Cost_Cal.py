from Network import *
from Network.CreateMaps import generate_network
from Network.Node import Node
from Network.Edge import BaseStation
from Network.Network import Network

nodes_BSs = generate_network(200, 10, 800)
print(nodes_BSs)
nodes = nodes_BSs[0]
BSs = nodes_BSs[1]
print(nodes, BSs)

off_s = []
for i in range(len(nodes)):
    off_s.append(1)

def calculate_off_delay(nodes:list, BSs:list, off_strategies:list):
    node_list = []
    for node in nodes:
        node_list.append(Node(node[0], node[1]))
    for i in range(len(nodes)):
        node_list[i].index = i

    BS_list = []
    for BS in BSs:
        BS_list.append(BaseStation(BS[0], BS[1]))
    for i in range(len(BS_list)):
        BS_list[i].index = i


    links = Network(node_list, BS_list)

    for i in range(len(off_strategies)):
        node_list[i].offload_decision = off_strategies[i]

    for node in node_list:
        if node.offload_decision == 0:
            

    for node in node_list:
        if node.offload_decision == 0:
            node.true_delay = node.task / node.cal_capacity
        else:








calculate_off_delay(nodes, BSs, off_s)