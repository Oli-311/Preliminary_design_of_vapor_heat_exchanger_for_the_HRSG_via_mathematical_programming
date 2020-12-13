import numpy as np
from pandas import read_csv


class funGen(object):

    def __init__(self, filename, lenth):
        self.x = -1
        self.y = -1
        self.lenth = lenth
        self.filename = filename
        self.data = []
        self.x_axe = []
        self.y_axe = []

        self.readFile()

        self.x_max = np.max(self.x_axe)
        self.y_max = np.max(self.y_axe)
        # print(self.x_max, self.y_max)

    def readFile(self):
        f = open(self.filename, encoding='UTF-8')
        names = []
        for i in range(self.lenth):
            names.append(str(i + 1))
        self.data = np.array(read_csv(f, names=names))
        self.x_axe = self.data[1, 1:]
        # print(self.x_axe)
        self.y_axe = self.data[2:, 0]
        # print(self.y_axe)
        self.data = self.data[2:, 1:]
        # print(self.data)

    def getData(self, x, y):
        self.x = x
        self.y = y
        pos = self.posFind()
        if len(pos) != 2:
            return 1
        # print(pos)
        a = 0
        b = 0
        data_1, data_2, data_3, data_4 = self.data[pos[1][0]+a][pos[0][0]+b], self.data[pos[1][0]+a][pos[0][1]+b], self.data[pos[1][1]+a][pos[0][0]+b], self.data[pos[1][1]+a][pos[0][1]+b]
        # print(data_1, data_2, data_3, data_4)
        prop_x = (self.x - self.x_axe[pos[0][0]]) / (self.x_axe[pos[0][1]] - self.x_axe[pos[0][0]])
        # print(prop_x)
        prop_y = (self.y - self.y_axe[pos[1][0]]) / (self.y_axe[pos[1][1]] - self.y_axe[pos[1][0]])
        # print(prop_y)
        res_temp_1 = data_1 + (data_3 - data_1) * prop_y
        res_temp_2 = data_2 + (data_4 - data_2) * prop_y
        res = res_temp_1 + (res_temp_2 - res_temp_1) * prop_x
        return res


    def posFind(self):
        pos_res = []
        # print(self.x, self.y)
        for i in range(len(self.x_axe) - 1):
            if self.x_axe[i] <= self.x < self.x_axe[i+1]:
                pos_res.append([i, i+1])
                break
            else:
                continue


        for i in range(len(self.y_axe) - 1):
            if self.y_axe[i] <= self.y < self.y_axe[i+1]:
                pos_res.append([i, i+1])
                break
            else:
                continue
        return pos_res


if __name__ == '__main__':
    func_a = funGen("NUT_croise.csv", 6)
    data = np.array(func_a.data)
    print(func_a.getData(0.375, 6.5))

