import GeoClass
import MatProp
import linFunGen as Lin
import HRSGProp

import numpy as np
flow_rate = 143.1708


def f(n, m, D, L, e1, e2):
    a = GeoClass.SteamGeometry

    E = Lin.funGen("NUT_croise.csv", 6)
    G_steam = GeoClass.SteamGeometry(D, L, flow_rate, n, m)    # D,L,Dm,n,m

    G_air = GeoClass.AirGeometry(D, L, 1120, e1, e2, n, m)    # D,L,Dm,e1,e2,n,m

    # print(G_air.D)

    steam1 = MatProp.Steam(G_steam, 6262.153, 0.5243, 7.94187 * 10 ** -5, 673.686)   # air_geo,c,lambda,mu,rho

    air1 = MatProp.Air(G_air, 1107.40, 0.059, 3.854 * 10 ** -5, 0.547)  # geo,c,lambda,mu,rho
    # print(steam1.Re, steam1.Pr)
    # print(air1.Re, air1.Pr)
    if 2000 > air1.Re or air1.Re > 20000:
        return -1, -1




    H = HRSGProp.HRSG(air1, G_air, steam1, G_steam, 1, E)
    # print(H.e)

    q_gas = n * air1.h * G_air.Sl * ((2-H.e) / 2) * (838 - 595.58)

    # print(q_gas / 1000)
    return H.e, q_gas / 1000\

def period(n, m, D, L):
    temp = 100000000000000000000000000
    res = []
    e1 = 1.01 * D
    e2 = 1.01 * D
    for i in range(125):
        e2 = 1.01 * D
        for j in range(125):
            try:
                eta, q_gas = f(n, m, D, L, e1, e2)
                if eta != -1 and q_gas != -1:
                    # print(e1, e2, eta, abs(q_gas - 276494.4))
                    # print(e1, e2, eta, abs(q_gas - 276494.4), file=doc)
                    if abs(q_gas - 276494.4) < temp:
                        temp = abs(q_gas - 276494.4)
                        res = [e1/D, e2/D,abs(q_gas - 276494.4)]

            except:
                pass
            e2 += 0.0005
        e1 += 0.0005
    print(res)

if __name__ == "__main__":
    n = 3000
    m = 70
    D = 0.05
    L = 50

    # doc = open('output.txt', 'w')
    period(n, m, D, L)


