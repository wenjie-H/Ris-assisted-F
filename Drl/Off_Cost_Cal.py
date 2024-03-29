from EdgeNetwork import *
from EdgeNetwork.CreateMaps import generate_network
from EdgeNetwork.WNode import Node
from EdgeNetwork.Edge import BaseStation
from EdgeNetwork.Network import Network
import logging
import random



def calculate_off_delay(nodes:list, BSs:list, off_strategies:list):


    node_list = []
    for node in nodes:
        node_list.append(Node(node[0], node[1]))
    for i in range(len(nodes)):
        node_list[i].index = i
    # logging.info('nodelist:'+str(len(node_list)))

    BS_list = []
    for BS in BSs:
        BS_list.append(BaseStation(BS[0], BS[1]))
    for i in range(len(BS_list)):
        BS_list[i].index = i


    links = Network(node_list, BS_list)

    for i in range(len(off_strategies)):
        node_list[i].offload_decision = off_strategies[i]

    for node in node_list:
        if node.offload_decision == 1:
            dis_node_BS_list = []
            for BS in BS_list:
                dis_node_BS = ((node.position_x - BS.position_x)**2 + (node.position_y - BS.position_y)**2)**(1/2)
                dis_node_BS_list.append(dis_node_BS)

            # logger.info('dis:' + str(min(dis_node_BS_list)))
            target_BS = dis_node_BS_list.index(min(dis_node_BS_list))
            node.off_BS_index = target_BS
            BS_list[target_BS].cal_load += 1

    for node in node_list:
        if node.offload_decision == 0:
            node.true_delay = node.task / node.cal_capacity
        else:
            node.true_delay = node.task * BS_list[node.off_BS_index].cal_load / BS_list[node.off_BS_index].cal_capacity + \
                              node.task * links.link_load_d2i[node.index][node.off_BS_index] / links.link_d2i[node.index][node.off_BS_index]

    sum_delay = 0
    for node in node_list:
        sum_delay += node.true_delay

        # logging.info('node:' + str(node.index) + '---' + str(node.task) + '---' + str(node.offload_decision) + '---' + str(node.task * BS_list[node.off_BS_index].cal_load / BS_list[node.off_BS_index].cal_capacity) + ',' + str(node.task * links.link_load_d2i[node.index][node.off_BS_index] / links.link_d2i[node.index][node.off_BS_index]) + '---' + str(node.index) + '---' + str(node.true_delay))
        # print('node:', node.index, node.off_BS_index, node.true_delay)
    return sum_delay


if __name__ == '__main__':
    logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='w')
    ch = logging.StreamHandler()
    logger = logging.getLogger()
    logger.addHandler(ch)

    nodes_BSs = generate_network(20, 16, 800)
    print(nodes_BSs)
    nodes = nodes_BSs[0]
    BSs = nodes_BSs[1]
    print(nodes, BSs)

    off_s = []
    for i in range(len(nodes)):
        off_s.append(random.randint(0, 1))

    calculate_off_delay(nodes, BSs, off_s)