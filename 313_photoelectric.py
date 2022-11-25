import numpy as np
import math as mt
from matplotlib import pyplot as plt

planck = 4.135667516*10**(-15) #eV*s

wl = np.array([612, 518, 504, 457, 400]) #nm
sp = np.array([0.522, 0.928, 0.941, 1.008, 1.506]) #eV

c = 3*10**8 #m/s
V0 = np.zeros([len(wl)])
wlim = np.zeros([len(wl)])
fit = np.zeros(5)
for i in range(len(wl)):
    wlim[i] = wl[i]*10**(-9)
    V0[i] = c/wlim[i]

a,b = np.polyfit(V0,sp,1)

for m in range(len(wl)):
    fit[m] = V0[m]*a + b

fail = (abs(a-planck)/planck)*100

plt.plot(V0,fit,'r')
plt.scatter(V0,sp,c='b')
plt.grid()
plt.xlabel("frequency in Hz")
plt.ylabel("stopping potential in eV")



