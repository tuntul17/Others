import numpy as np
import math as mt

U = 4000 #V
me = 9.1*10**-31 #kg
e = 1.6*10**-19 #C
L = 125*10**-3 #m
r = 0.042 #m
h = 6.6*10**-34 #js


d = (h/(2*(2*U*me*e)**0.5))*((2*(L**2+r**2)**0.5)/((L**2+r**2)**0.5-L))**0.5 #m

res1 = d*10**9
