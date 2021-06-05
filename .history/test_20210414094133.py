import math
import numpy as np
import matplotlib.pyplot as plt

a = 40
X = np.ones(a)

for i in range(0,40):
    X[i] = i * 0.1


for i in range(1,a):
    #内层积分，积到x
    s = 0
    for j in range(0,i-1):
        s0 =Y[j+1] * ((1 / math.sqrt(X[i]-X[j+1])) + Y[j] * (1 / math.sqrt(X[i]-X[j])) * (X[j + 1] - X[j]) / (2))
        #s0 = (((Y0[j+1] + Y0[j]) * (X[j + 1] - X[j])) / (2))    #第(j+1)个梯形的面积
        s = s0 + s    #S为最后的积分
    #内层积分，积到x
    F[i] = (1/(2 * math.pi)) * s / 1200    #乘以外面的一个
    #求dp/p的值
    delta_P[i] = con * F[i]
    #扭曲后的x的值为x1
    X1[i] = (B * r0 - k * F[i] * math.sqrt(r0) + X[i])