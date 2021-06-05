import math
import numpy as np
import matplotlib.pyplot as plt

s = 0
dFy0 = [0,1,2,3,4,5,6,7,8,9]
L = np.zeros(10)
X = [0,1,2,3,4,5,6,7,8,9]
n0 = len(L)
for i in range(0,n0):
    X1[i] = X[i] + h / math.tan(miu)
#-------------将飞行器上的点投影到一条线上-----------------#
    C0[i][0] = X1[i]
    C0[i][1] = dFy0[i]

C2 = C0[np.lexsort(C0[:,::-1].T)]
X1[i] = np.ones(10)



for i in range(0,n0):
    dFy1[i] = C2[i][1]

for i in range(0,10):
    s = dFy1[i] + s
    L[i] = s

plt.plot(X,L)
plt.show()
