'''
激波修正
本程序用于修正激波的非线性扭曲效应，修正方法为HB方法
'''

import math
import numpy as np
import matplotlib.pyplot as plt

pressure = np.loadtxt("pressuremodel1.txt",dtype=np.float64)   #存放未修正的压力信号
a = len(pressure)                                              #未加点时的点数

X = np.ones(a,dtype=np.float64)     #存放x的数组 用于加点用的横坐标数组
Y = np.ones(a,dtype=np.float64)     #存放y的数组 用于加点用的纵坐标数组
b0 = 50                             #每一个 较大的距离之间增加的点数
x0 = np.zeros(b0+1,dtype=np.float64)
y0 = np.zeros(b0+1,dtype=np.float64)

#先将未修正压力信号存入X,Y中
for i in range(0,a):
    c = pressure[i][0]
    d = pressure[i][1]
    #ca = cau[i][1]
    X[i] = c
    Y[i] = d



#-------积分部分----------
F = np.ones(a, dtype=np.float64)
F[0] = 0
F[a-1] = 0
s = 0
for i in range(0,a-1):
    #if(X[i+1]>X[i]):
    s0 = 0.5 * (X[i+1] - X[i]) * (Y[i+1] + Y[i])
    #s0 = (((Y0[j+1] + Y0[j]) * (X[j + 1] - X[j])) / (2))    #第(j+1)个梯形的面积
    s = s0 + s    #S为最后的积分
    F[i] = s
    print(X[i],F[i])
    #if(X[i+1]<X[i])
#------积分部分-----------







#积分图像作图
plt.plot(X,F,'-o')
plt.show()



