import numpy as np


class SteamGeometry():
    def __init__(self, D, L, Dm, n, m):
        self.D = D
        self.L = L
        self.Sl = np.pi * D * L
        self.S = 0.25 * np.pi * D ** 2
        self.Dm = Dm

        self.n = n
        self.m = m


class AirGeometry():
    def __init__(self, D, L, Dm, e1, e2, n, m):
        self.D = D
        self.L = L
        self.Sl = np.pi * D * L
        self.e1 = e1
        self.e2 = e2
        self.Dm = Dm
        self.n = n
        self.m = m