import math
import numpy as np
import matplotlib.pyplot as plt

s = 0
dFy1 = [0,1,2,3,4,5,6,7,8,9]
L = np.zeros(10)
X = [0,1,2,3,4,5,6,7,8,9]
for i in range(0,10):
    L[i] = s
    s = dFy1[i] + s

plt.plot(X,L)
plt.show()
