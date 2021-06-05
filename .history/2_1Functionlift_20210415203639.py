#本程序实现求解无升力构型的F函数
#同时求解出未经修正的压力信号
#F函数是无量纲的

import math
import numpy as np
import matplotlib.pyplot as plt

#初始输入条件
M = 1.7                    #输入马赫数
P0 = 101325                 #输入飞行高度处的大气静压
gama = 1.4                  #比热比
B = math.sqrt(M * M - 1)    #修正因子
k = (1 / math.sqrt(2)) * (gama + 1) * M**4 * B**(-1.5)   #特征性系数k
r0 = 0.6299                      #r0为计算的位置  DWB为63.072  model1为20 2、3为10
con1 = (gama * M**2)/(math.sqrt(2 * B * r0))   #最后用来求压力的
con2 = B / (gama * P0 * M ** 2)

Lift = np.loadtxt("lift.txt",dtype=np.float64)     #存放升力分布的一阶导数数据文件
volume = np.loadtxt("se.txt",dtype=np.float64)   #存放体积分布的二阶导数数据文件
#cau = np.loadtxt("cauchy.txt",dtype=np.float64)      #积分含有哑元的存放

a = len(volume)        #a为b的长度
#print(a)              #检查文件长度
X = np.ones(a)     #存放x的数组
Y = np.ones(a)     #存放y的数组
Y0 = np.ones(a)    #存放含哑元的表达式的值
L = np.ones(a)
S_e = np.ones(a)

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


#------考虑升力分布的模块-------#
for i in range(0,a):
    L[i] = con2 * Lift[i]  #升力部分的二阶导数
    S_e[i] = L[i] + Y[i]   #计算等效截面积的二阶导数
#------考虑升力分布的模块--------#



#通过变上限积分求解F函数，积分使用梯形公式
F = np.ones(a, dtype=np.float64)   #产生一个长度为a的初始化数组
X1 = np.ones(a, dtype=np.float64)
delta_P = np.ones(a, dtype=np.float64)
X1[0] = 0.0        #强制F的第一个值为0
delta_P[0] = 0.0   #强制F的第一个值为0
F[0] = 0.0         #强制F的第一个值为0


for i in range(1,a):
    #----内层积分，积到x----#
    s = 0
    A = np.zeros(i)
    for j in range(0,i):
        if (j < i-1):
            A[j] = (S_e[j+1] * (1 / math.sqrt(X[i]-X[j+1])) + S_e[j] * (1 / math.sqrt(X[i]-X[j]))) \
            * (X[j + 1] - X[j]) / (2)
            s = A[j] + s
        if((j == i-1)and(i>5)):
            s = s + 2 * A[i-2] - A[i-3]
    #------------------#
    F[i] = (1/(2 * math.pi)) * s
    #求dp/p的值
    delta_P[i] = con1 * F[i]
    #扭曲后的x的值为x1
    X1[i] = (B * r0 - k * F[i] * math.sqrt(r0) + X[i])
    #print(X[i],F[i])
    #print(X1[i]-B * r0,delta_P[i])


#----------输出计算结果--------#
#绘制F函数的图像
plt.plot(X, F,'-o')
plt.xlabel("x/in")
plt.ylabel('F(y)')
plt.show()

X0 = np.zeros(a)
for i in range(1,a):
    X0[i] = X1[i] - B * r0

#绘制未修正的过压的图像
plt.plot(X0, delta_P,'-o',c='b')
plt.xlabel("x/in")
plt.ylabel('dp/p')
plt.show()

for i in range(1,a):
    print(X0[i],delta_P[i])

#delta_P = np.ones[a]    #储存过压的数组
#delta_P[i] = P0 * ((gama * M * M)/(math.sqrt(2 * B * r0))) * F[i]