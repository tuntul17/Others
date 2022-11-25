import numpy as np
from time import *
from pylab import *
N = arange(0,6)
starttime = np.zeros(len(N))
lasttime = np.zeros(len(N))
mypi = np.zeros(len(N))
for i in range(0,6):
    N[i] = int(10**(i+1))
for k in range(0,len(N)):
    starttime[k] = clock()
    inside= 0
    x = np.random.rand(N[k],1)
    y = np.random.rand(N[k],1)
    for m in range(0,N[k]):
        if (x[m])**2 + (y[m])**2 <=1:
            inside = inside +1
        mypi[k] = 4*(inside/N[k])
    lasttime[k] = (clock() - starttime[k])
print(mypi)
plot(N,mypi)
show()