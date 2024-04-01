import random
class BaseStation:
    def __init__(self, pos_x, pos_y):
        self.position_x = pos_x
        self.position_y = pos_y

        self.each_layer_vehicles = [[], [], [], [], [], [], [], [], [], []]
        self.para_num = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.off_vehicles = []
        self.cal_load = 1

        self.cal_num = 15

        self.cal_capacity = 0
        self.cal_num_capacity = 0
        self.index = 0
        self.initCal1()



    def initCal1(self):
        self.cal_capacity = 50
        self.cal_num_capacity = 20
