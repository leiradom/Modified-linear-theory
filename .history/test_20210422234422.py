import math
import numpy as np
import matplotlib.pyplot as plt

s = 0
dFy0 = [0,1,2,3,4,5,6,7,8,9]
L = np.zeros(10)
X = [0,1,2,3,4,5,6,7,8,9]
n0 = len(L)
C0 = np.zeros((10,2))

for i in range(0,n0):
#-------------将飞行器上的点投影到一条线上-----------------#
    C0[i][0] = X[i]
    C0[i][1] = dFy0[i]

C2 = C0[np.lexsort(C0[:,::-1].T)]

for i in range(0,n0):
    dFy1[i] = C2[i][1]

for i in range(0,10):
    s = dFy0[i] + s
    L[i] = s

plt.plot(X,L)
plt.show()
