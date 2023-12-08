from typing import List
from Node import Node
from Edge import BaseStation
from Shannon import Shannon
from copy import deepcopy
# from
from Parameters import Max_layer
# from CreateVehicleBS import CreateVehicleBSs, CreateVehicleBSsV2VNew, GetVehicleData, GetCandiVehicleData
import copy

class Network():
    def __init__(self, nodes: List[Node], BSs: List[BaseStation]):
        self.nodes = nodes
        self.BSs = BSs
        self.link_d2d = []
        self.link_load_d2d =[]
        self.link_d2i = []
        self.link_load_d2i = []

        self.initLink()

    def initLink(self):
        for node1 in self.nodes:
            device_device_link = []
            device_device_load = []
            for node2 in self.nodes:
                device_device_link.append(Shannon(node1.position_x, node2.position_x, node1.position_y, node2.position_y))
                device_device_load.append(1)
            self.link_d2d.append(device_device_link)
            self.link_load_d2d.append(device_device_load)

        for node in self.nodes:
            BS_device_link = []
            BS_device_load = []
            for BS in self.BSs:
                BS_device_link.append(Shannon(node.position_x, BS.position_x, node.position_y, BS.position_y))
                BS_device_load.append(1)
            self.link_d2i.append(BS_device_link)
            self.link_load_d2i.append(BS_device_load)

    def clear_load(self):
        for i in range(len(self.link_load_d2i)):
            for j in range(len(self.link_load_d2i[0])):
                self.link_load_d2i[i][j] = 1

        for i in range(len(self.link_load_d2d)):
            for j in range(len(self.link_load_d2d[0])):
                self.link_load_d2d[i][j] = 1











if __name__ == '__main__':

    pass