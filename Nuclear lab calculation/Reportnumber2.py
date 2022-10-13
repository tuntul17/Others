import numpy as np
import math as mt
from pylab import *
import csv
import statistics as st
from scipy.optimize import curve_fit

#İMPORTİNG DATA FROM .CSV FILEs
file = open("Lab2.csv")
type(file)
csvread = csv.reader(file)
header = []
header = next(csvread)
header
rows = []
for row in csvread:
    rows.append(row)
rows
file.close()
#PREPARING THE DATA
N0 = np.zeros(len(rows))

for i in range(len(N0)):
    N0[i] = rows[i][0]  
N0_srtd = np.sort(N0)

#AVERAGE VALUE
n_av = sum(N0)/len(N0)

#STANDARD DEVIATION
"""add = 0.
sigsqr= 0.
for i in range(len(N0)):
    add += (N0[i]-n_av)**2
sigsqr = (add/(len(N0)-1))**0.5"""

sig = st.stdev(N0,n_av)

n = n_av**0.5

#Stdev Vs. n_av sqrroot

DIFF = (abs(sig-n)/sig)*100
Pn = np.zeros(len(N0))
#GUSS DISTRIBUTION:
for i in range(len(N0)):
    Pn[i] = (1/(2*mt.pi*sig)**0.5)*mt.exp(-(N0_srtd[i]-n_av)**2/(2*sig**2))
def diff(n,A,avn, sg):
    y = A*np.exp(-(n-avn)**2/(2*sg**2))
    return y
A = 1/(2*mt.pi*sig)**0.5
Pin = diff(N0_srtd,A,n_av,sig)




k = np.linspace(0,59,59)
scatter(k,Pin,c = "r", alpha = 0.8)




#scatter(k,Pn,c = "r", alpha = 1, s = 1.2)