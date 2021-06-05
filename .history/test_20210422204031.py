import math
import numpy as np
import matplotlib.pyplot as plt

n0 = 5

X1 = np.array([[11,52],[5,122],[1,20]])


X2 = X1[np.lexsort(X1[:,::-1].T)]
print(X2)


'''
for i in range(0, n0 - 1):
    for j in range(0, n0 - i - 1):
        if(X1[j] > X1[j+1]):
            X1[j],X1[j+1] = X1[j+1],X1[j]
            #dFy0[j],dFy0[j+1] = dFy0[j+1],dFy0[j]
print(X1)
'''

