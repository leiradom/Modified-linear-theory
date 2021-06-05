import math 
import numpy as np
import matplotlib.pyplot as plt

b = np.loadtxt("ex.txt",dtype=np.float64)

a = len(b)
print(a)           #a的值为1001
X = np.ones(1001)
Y = np.ones(1001)
B = np.ones(1001)
for i in range(0,a):
    c = b[i][0]
    d = b[i][1]
    X[i] = c
    Y[i] = d
print(X)      #C是x
print(Y)      #D是y

S = np.ones(1001)

for i in range(0,a):
    x = X[i]
    S = 0
    for j in range(0,i):
        s0 = ((Y[j+1] + Y[j]) * (X[j + 1] - X[j])) / (2)    #第(i+1)个梯形的面积
        S = s0 + S    #S为最后的积分
    S[i] = S