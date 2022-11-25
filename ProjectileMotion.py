from numpy import *
from math import *
from pylab import *

g = 9.81
v = float(input("velocity: "))
theta = radians(float(input("angle: ")))
theta2 = radians(float(input("angle: ")))
t = 2*v*sin(theta)/g
t2 = 2*v*sin(theta2)/g

step = 10000
rate= t/step
rate2 = t2/step
tarr = zeros(step)
T = zeros(step)
y = zeros(step) 
x = zeros(step) 
x1 = zeros(step)
y1 = zeros(step)
for i in range(step):
    tarr[i] = i*rate
    T[i] = i*rate2
def Xpos(t,theta):
    X = v*cos(theta)*t
    return X
def Ypos(t,theta):
    Y = v*sin(theta)*t -0.5*g*t**2
    return Y

for k in range(step):
    x[k] = Xpos(tarr[k],theta)
    y[k] = Ypos(tarr[k],theta)
    x1[k] =Xpos(T[k],theta2)
    y1[k] = Ypos(T[k],theta2)
   # if (y1[k] <=0):
    #    y1[k] = 0
     #   x1[k] = 0
xlabel("distence")
ylabel("height")
plot(x,y,x1,y1)

show()