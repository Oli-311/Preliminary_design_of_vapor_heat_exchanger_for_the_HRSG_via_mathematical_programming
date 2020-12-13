import KrFunc
import numpy as np

class Air():
    def __init__(self, air_geo, c, lumb, mu, rho):
        self.c = c
        self.v_eq = air_geo.Dm / (rho * air_geo.m * air_geo.L * (air_geo.e1 - air_geo.D))
        # self.v_eq = 4 * air_geo.Dm / (air_geo.n * np.pi * air_geo.D ** 2)
        self.lumb = lumb
        self.mu = mu
        self.rho = rho
        self.Pr = mu * c / lumb
        self.Re = self.RE(air_geo)
        self.Kr = self.KR(air_geo)
        self.Km = self.KM(air_geo)

        self.Nu = 0.33 * self.Kr * self.Km * self.Pr ** 0.33 * self.Re ** 0.6
        self.h = self.Nu * lumb / air_geo.D

    def RE(self, air_geo):
        # print(self.v_eq * self.rho * air_geo.D / self.mu)
        return self.v_eq * self.rho * air_geo.D / self.mu

    def KM(self, air_geo):
        l = [0.67, 0.76, 0.82, 0.87, 0.92, 0.94, 0.96, 0.98, 0.99, 1]
        if air_geo.m - 1 >= 10:
            return 1
        return l[air_geo.m - 1]

    def KR(self, air_geo):      # 待添加
        func_kr = KrFunc.FuncKr(air_geo.e1, air_geo.e2, air_geo.D, self.Re)
        # print(func_kr.Kr, func_kr.out_range_mark)
        return func_kr.Kr


class Steam():
    def __init__(self, geo, c, lumb, mu, rho):
        self.c = c
        self.lumb = lumb
        self.mu = mu
        self.rho = rho
        self.v = geo.Dm / (geo.S * geo.n * self.rho)
        self.Re = self.v * rho * geo.D / mu
        self.Pr = mu * c / lumb
        self.Nu = self.Nu(self.Re, self.Pr)
        self.h = self.Nu * lumb / geo.D

    def Nu(self, Re, Pr):
        if 0.7 < Pr and 10 ** 4 < Re:
            # print("Re,Pr:", Re, Pr)
            return 0.023 * Re ** 0.8 * Pr ** 0.4
        else:
            # print("Re,Pr:", Re, Pr)
            return None