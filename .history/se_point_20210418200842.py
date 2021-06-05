#给二阶导数加点

import math
import numpy as np
import matplotlib.pyplot as plt


se = np.loadtxt("se.txt",dtype=np.float64)   #存放体积分布的数据文件

a = len(se)
X = np.ones(a)     #存放x的数组
Y = np.ones(a)     #存放y的数组
b0 = 20                             #每一个 较大的距离之间增加的点数
x0 = np.zeros(b0+1,dtype=np.float64)
y0 = np.zeros(b0+1,dtype=np.float64)
X1 = np.zeros(1,dtype=np.float64)
Y1 = np.zeros(1,dtype=np.float64)


for i in range(0,a):
    c = se[i][0]
    d = se[i][1]
    #ca = cau[i][1]
    X[i] = c
    Y[i] = d


for i in range(0,a-1):
    #li = math.sqrt((X[i+1] - X[i])**2 + (Y[i+1] - Y[i])**2)
    k0 = ((Y[i+1] - Y[i])/(X[i+1] - X[i]))  #两点间的斜率
    h0 = ((X[i+1] - X[i])/(b0))   #每一个都离散成b个点
    x0[0] = X[i]
    X1 = np.append(X1,x0[0])
    y0[0] = Y[i]
    Y1 = np.append(Y1,y0[0])
    for j in range(1,b0):
        x0[j] = x0[j-1] + h0
        X1 = np.append(X1,x0[j])
        y0[j] = y0[j-1] + k0 * (x0[j] - x0[j-1])
        Y1 = np.append(Y1,y0[j])


plt.plot(X1,Y1,c='b')
#plt.plot(X,Y,c='r')
plt.show()