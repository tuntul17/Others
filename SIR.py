import numpy as np
from matplotlib import pyplot as plt


a = 0.7
b = 0.2

S = np.zeros(50)
I = np.zeros(50)
R = np.zeros(50)

t = 0

S[t] = 0.99
I[t] = 0.01
R[t] = 0.

for i in range(0,49):
    S[t+1] = S[t] -a*I[t]*S[t]
    I[t+1] = I[t] + a*I[t]*S[t] - b*I[t]
    R[t+1] = R[t] + b*I[t]
    t +=1
    
    
plt.plot(S)
plt.plot(I)
plt.plot(R)
plt.show()