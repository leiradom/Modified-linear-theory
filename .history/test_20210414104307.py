import math
import numpy as np
import matplotlib.pyplot as plt

a = 40
X = np.ones(a)
Y = np.ones(a)
F = np.zeros(a)

for i in range(0,40):
    X[i] = i * 0.1

for i in range(1,a):
    #内层积分，积到x
    s = 0
    A = np.zeros(i)
    for j in range(0,i-1):
        A[j] = ((1 / math.sqrt(X[i]-X[j+1])) + (1 / math.sqrt(X[i]-X[j]))) * (X[j + 1] - X[j]) / (2)
        #s0 = (((Y0[j+1] + Y0[j]) * (X[j + 1] - X[j])) / (2))    #第(j+1)个梯形的面积
        s = A[j] + s    #S为最后的积分
    #内层积分，积到x
    F[i] = s + (2 * A[i-2] - A[i-3])
    print(F[i])


