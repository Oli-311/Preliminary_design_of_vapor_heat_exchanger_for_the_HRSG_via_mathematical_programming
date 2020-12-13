import numpy as np


class HRSG():
    def __init__(self, air, G_air, steam, G_steam, PIN, E):
        self.KS = air.h * G_air.Sl * steam.h * G_steam.Sl * G_air.n / (air.h * G_steam.Sl + steam.h * G_air.Sl)
        self.NUT = self.KS / np.min([air.c, steam.c])
        self.R = np.minimum(air.c, steam.c) / np.maximum(air.c, steam.c)
        self.E = E
        self.e = self.func_e(self.NUT, self.R)
        self.DeltaT = PIN * self.e

    def func_e(self, NUT, R):
        # print(self.KS, R, NUT)
        return self.E.getData(R, NUT)