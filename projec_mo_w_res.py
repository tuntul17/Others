from math import *
from numpy import *
from pylab import *

k = 0.7
g = 9.81
m = 10 #input!
V_in = 10. #input!
theta = radians(float(37)) #input!
dt = 0.01

#initial locations
N = 1000    

#DtVy = -g -(k/m)*Vy
def fVy(V_in,theta):
    
    Vy0 = zeros(N)
    Vy0[0] = V_in*sin(theta)
     
    for i in range(N-1):
        Vy0[i+1] = Vy0[i] - (dt)*(g+k*Vy0[i]/m)
       
    return Vy0

#DtVx = -(k/m)*Vx
def fVx(V_in, theta):
    
    Vx0 = zeros(N)
    Vx0[0] = V_in*cos(theta)
    
    for j in range(N-1):
        Vx0[j+1] = Vx0[j] - dt *( Vx0[j]*(k))/m
        
    return Vx0
#vertical speed 
Vy = fVy(V_in,theta)
#horizontal speed
Vx = fVx(V_in,theta)




x = zeros(N)
y = zeros(N)
t = 0
for k in range(N):
  
    x[k] = Vx[k]*t
    y[k] = Vy[k]*t -0.5*g*t**2
    if y[k] < 0:
        break
    t = dt +t 

#plot(x,y)

#plot(Vx)
#plot(Vy)

plot(x,y)
"""
N = 150
x = zeros(N)
y = zeros(N)

t =0.
for m in range(N):
    x[m] = Vx[m]*t
    y[m] = Vy[m]*t -0.5*g*t
    t = t + dt
"""   
    





"""def FVy(V_in,theta):
    Vy = [V_in*sin(theta)]
    N = len(t)
    for i in range(N):
         Vy.append(Vy[i]-dt*(g+(k/m)*Vy[i]))
         if Vy[i] <= 0:
             break
    return Vy
Vy = FVy(V_in,theta)
def FVx(V_in,theta):
    Vx = [V_in*cos(theta)]
    
    N = len(t)
    for i in range(N):
        Vx.append(Vx[i]-dt*((k/m)*Vx[i]))  
    return Vx
Vx = FVx(V_in,theta)
"""


"""vx = V[0]
vy = V[1]
def Xpos(t):
    for k in range(length(Vx)):
        x.append(vx[k]*t[k])
    return x"""
