import numpy as np
from matplotlib import pyplot as plt
import math as mt

N = np.array([0,1,2,12,9,17,14,9,6,8,3,8,5,0,2,1,1,1,0,0,0,0,0,0])
x = np.zeros(24)
del_V = 0.099
f = np.zeros(24)
for i in range(len(N)):
    f[i] = N[i]/(sum(N)*del_V)
    x[i] = del_V*i

y = np.zeros(24)
Vmax2= (del_V*6)**2
for m in range(24):
   y[m] = pow(2/mt.pi,1/2)*pow(2/Vmax2,3/2)*mt.exp(-(del_V*m)**2/Vmax2)*(del_V*m)**2


plt.plot(x,f,'r+')
plt.plot(x,y)