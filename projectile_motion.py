import matplotlib.pyplot as plt
import math as m
import numpy as np
h = 0
g = 9.81
V = 10
A = m.pi/4 #theta
def Vy(V,A,t):
    vy = V*m.sin(A)-g*t
    return vy

def Vx(V,A,t):
    vx = V*m.cos(A)
    return vx

def posX(V,A,t):
    xpos= (V*m.cos(A))*t
    return xpos
def posY(V,A,t):
    ypos = h + (V*m.sin(A))*t -0.5*g*(t**2)
    return ypos

YPOS = np.zeros(10)
XPOS = np.zeros(10)
VX = np.zeros(10)
VY = np.zeros(10)
for t in range(0,10):
    YPOS = posY(V,A,t)
    XPOS[t] = posX(V,A,t)
    VX[t] = Vx(V,A,t)
    VY[t] = Vy(V,A,t)
    
plt.plot(XPOS,YPOS)

plt.plot(VX)
plt.plot(VY)
plt.show()