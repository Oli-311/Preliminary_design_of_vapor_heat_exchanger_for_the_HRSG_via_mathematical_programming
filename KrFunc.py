import numpy as np


class FuncKr:
    def __init__(self, e1, e2, D, Re):
        self.data = np.array([[[1.06, 1.04, 1.00], [0.95, 0.96, 0.95], [0.73, 0.83, 0.94], [0.66, 0.81, 0.91]],
                              [[1.06, 1.05, 1.00], [0.95, 0.96, 0.95], [0.73, 0.83, 0.90], [0.66, 0.81, 0.91]],
                              [[1.07, 1.03, 1.00], [1.03, 1.01, 1.00], [0.98, 1.00, 1.00], [0.95, 1.02, 1.02]],
                              [[1.00, 0.98, 0.95], [1.03, 1.01, 0.98], [1.08, 1.02, 1.00], [1.00, 1.02, 1.00]]])
        self.e1_D = e1 / D
        self.e2_D = e2 / D
        self.Re = Re

        self.out_range_mark = 0
        self.e1_axe = [1.25, 1.5, 2, 3]
        self.e2_axe = [1.25, 1.5, 2, 3]
        self.re_axe = [2000, 8000, 20000]
        self.pos_e1 = self.Pos_e1()
        self.pos_e2 = self.Pos_e2()
        self.pos_re = self.Pos_re()
        self.Kr = self.getData()

    def Pos_e1(self):
        if 1.25 <= self.e1_D <= 1.5:
            return [0, 1]
        elif 1.5 <= self.e1_D <= 2:
            return [1, 2]
        elif 2 <= self.e1_D <= 3:
            return [2, 3]
        else:
            self.out_range_mark = 1
            return []

    def Pos_e2(self):
        if 1.25 <= self.e2_D <= 1.5:
            return [0, 1]
        elif 1.5 <= self.e2_D <= 2:
            return [1, 2]
        elif 2 <= self.e2_D <= 3:
            return [2, 3]
        else:
            self.out_range_mark = 1
            return []

    def Pos_re(self):
        if 2000 <= self.Re <= 8000:
            return [0, 1]
        elif 8000 <= self.Re <= 20000:
            return [1, 2]
        else:
            self.out_range_mark = 1
            return []

    def getData(self):
        if self.out_range_mark == 1:
            return 1

        temp_1 = (self.data[self.pos_e1[1]] - self.data[self.pos_e1[0]]) * (self.e1_D - self.e1_axe[self.pos_e1[0]]) / (
                    self.e1_axe[self.pos_e1[1]] - self.e1_axe[self.pos_e1[0]]) + self.data[self.pos_e1[0]]
        temp_2 = (temp_1[self.pos_e2[1]] - temp_1[self.pos_e2[0]]) * (self.e2_D - self.e2_axe[self.pos_e2[0]]) / (
                    self.e2_axe[self.pos_e2[1]] - self.e2_axe[self.pos_e2[0]]) + temp_1[self.pos_e2[0]]
        Kr = (temp_2[self.pos_re[1]] - temp_2[self.pos_re[0]]) * (self.Re - self.re_axe[self.pos_re[0]]) / (
                    self.re_axe[self.pos_re[1]] - self.re_axe[self.pos_re[0]]) + temp_2[self.pos_re[0]]
        return Kr


if __name__ == '__main__':
    a = FuncKr(0.075, 0.1, 0.05, 8000)
    print(a.Kr)
