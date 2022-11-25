import numpy as np
import math as mt

d = 17*pow(10,3) #metre

He_red = np.array([57.52,10.28])
He_yel =([53.63,12.34])
He_gre = np.array([49.82,14.56])
Na_1 = np.array([52.88, 12.97])
Na_2 = np.array([54.44, 13.95])
Na_3 = np.array([51.86, 15.09])
Hg_1 = np.array([54.13, 11.02])
Hg_2 = np.array([55.68,11.75])
Hg_3 = np.array([52.99, 12.23])

lam = np.zeros(9)


lam[0] = d*mt.sin(mt.radians(abs((He_red[1] - He_red[0])/2)))
lam[1] = d*mt.sin(mt.radians(abs(He_yel[0] - He_yel[1])/2))
lam[2] = d*mt.sin(mt.radians(abs(He_gre[0] - He_gre[1])/2))
lam[3] = d*mt.sin(mt.radians(abs(Na_1[0] - Na_1[1])/2))
lam[4] = d*mt.sin(mt.radians(abs(Na_2[0] - Na_2[1])/2))
lam[5] = d*mt.sin(mt.radians(abs(Na_3[0] - Na_3[1])/2))
lam[6] = d*mt.sin(mt.radians(abs(Hg_1[0] - Hg_2[1])/2))
lam[7] = d*mt.sin(mt.radians(abs(Hg_2[0] - Hg_2[1])/2))
lam[8] = d*mt.sin(mt.radians(abs(Hg_3[0] - Hg_3[1])/2))

for i in range(len(lam)):
    print(lam[i]*10**(-1),"nm")