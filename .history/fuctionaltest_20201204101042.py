#本程序实现求解无升力构型的F函数
#同时求解出近场的压力信号

import math
import numpy as np
import matplotlib.pyplot as plt


X = np.ones(501)

#提取体积分布数据中的两列数据
for i in range(0,501):
    c = 0.01 * i
    X[i] = c
    #Y0[i] = ca

a = len(X)
print(X)
#print(Y)

#通过变上限积分求解F函数，积分使用梯形公式
F = np.ones(a,dtype=np.float64)   #产生一个长度为a的初始化数组
F[0] = 0         #强制F的第一个值为0

for i in range(1,a):
    #内层积分，积到x
    s = 0
    for j in range(0,i-1):
        s0 =((1 / math.sqrt(X[i]-X[j+1])) + (1 / math.sqrt(X[i]-X[j])) * (X[j + 1] - X[j]) / (2))
        #s0 = (((Y0[j+1] + Y0[j]) * (X[j + 1] - X[j])) / (2))    #第(j+1)个梯形的面积
        s = s0 + s    #S为最后的积分
    #内层积分，积到x
        F[i] = s
print(F)


#绘制F函数的图像
plt.plot(X,F)
plt.show()
