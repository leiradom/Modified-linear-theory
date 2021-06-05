#本程序实现求解无升力构型的F函数
#同时求解出近场的压力信号

import math
import numpy as np
import matplotlib.pyplot as plt


M = 1.26                    #输入马赫数
P0 = 101325                 #输入大气静压
gama = 1.4                  #比热比
B = math.sqrt(M * M - 1)    #修正因子
k = (1 / math.sqrt(2)) * (gama + 1) * M**4 * B**(-1.5)   #特征性系数k
r0 = 10                     #r0为计算的位置


volume = np.loadtxt("volume.txt",dtype=np.float64)   #存放体积分布的数据文件
#Lift = np.loadtxt("volume.txt",dtype=np.float64)    #存放升力分布的数据文件
#cau = np.loadtxt("cauchy.txt",dtype=np.float64)      #积分含有哑元的存放

a = len(volume)        #a为b的长度
#print(a)              #检查文件长度

X = np.ones(a)     #存放x的数组
Y = np.ones(a)     #存放y的数组
Y0 = np.ones(a)    #存放含哑元的表达式的值
B = np.ones(a)     #

#提取体积分布数据中的两列数据
for i in range(0,a):
    c = volume[i][0]
    d = volume[i][1]
    #ca = cau[i][1]
    X[i] = c
    Y[i] = d
    #Y0[i] = ca

#print(X)
#print(Y)

#通过变上限积分求解F函数，积分使用梯形公式
F = np.ones(a,dtype=np.float64)   #产生一个长度为a的初始化数组
F[0] = 0         #强制F的第一个值为0

for i in range(1,a):
    F[i] = 2*i**2* Y[i]   #乘以外面的一个


#绘制F函数的图像
plt.plot(X,F)
plt.show()

delta_P = np.ones[a]    #储存过压的数组
delta_P[i] = P0 * ((gama * M * M)/(math.sqrt(2 * B * r0))) * F[i]