#该程序用于验证变上限积分的数值解法

import math 
import numpy as np
import matplotlib.pyplot as plt

b = np.loadtxt("ex.txt",dtype=np.float64)   #包含了500个点，计算从1-e5的值
a = len(b)        #a为b的长度

#print(a)           #a的值为501
X = np.ones(a)     #存放x的数组
Y = np.ones(a)     #存放y的数组

B = np.ones(a)     #

for i in range(0,a):
    c = b[i][0]
    d = b[i][1]
    X[i] = c
    Y[i] = d
#print(X)      #C是x
#print(Y)      #D是y

S = np.ones(a,dtype=np.float64)
F = np.ones(a,dtype=np.float64)   #产生一个长度为a的初始化数组
F[0] = 0         #强制F的第一个值为0

#print(F)        #验证F的正确性



for i in range(1,a):
    s = 0
    for j in range(0,i):
        s0 = ((Y[j+1] + Y[j]) * (X[j + 1] - X[j])) / (2)    #第(j+1)个梯形的面积
        s = s0 + s    #S为最后的积分
    F[i] = s

print(F)


