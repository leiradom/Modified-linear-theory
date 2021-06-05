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
'''
#没问题
X0 = X
Y0 = Y
'''

#------------1先找出第一个强间断的地方,已经核实，l0没有问题
for i0 in range(0,a-1):
    if(math.sqrt((X[i0+1] - X[i0])**2 + (Y[i0+1] - Y[i0])**2) >1.2):   #1.3
    #if((X[i+1] - X[i]) * (Y[i+1] - Y[i])):
        #px = i0                            #记录此时的i
        #print(px,X[i0])
        l00 = math.sqrt((X[i0+1] - X[i0])**2 + (Y[i0+1] - Y[i0])**2)
        l0 = l00 / 20                     #判断是否要插值的距离 只要大于20倍的最大距离，就要增加点数
        #h0 = ((X[i0+1] - X[i0])/(b0)) 
        #k0 = ((Y[i0+1] - Y[i0])/(X[i0+1] - X[i0]))  #两点间的斜率
        '''
        #x0[0] = X[i0]
        #y0[0] = Y[i0]
        for j in range(1,b0):
            x0[j] = x0[j-1] + h0
            y0[j] = y0[j-1] + k0 * (x0[j] - x0[j-1])
            print(x0[j],y0[j])
        for k in range(1,b0):
            X = np.insert(X,i0+k,x0[k])
            Y = np.insert(Y,i0+k,y0[k])
        #print(Y[i0]+k0*h0)    
        '''
        break
#------------print(l00) #检验是不是，验证了，就是

print(l0)



#2---------------------给距离较大的地方都进行加点
for i in range(0,a-1):
    li = math.sqrt((X[i+1] - X[i])**2 + (Y[i+1] - Y[i])**2)
    k0 = ((Y[i+1] - Y[i])/(X[i+1] - X[i]))  #两点间的斜率
    #先找到距离较大的点
    if((li >= l0)):
        px = i                       #记录每一个距离较大的地方的i
        h0 = ((X[i+1] - X[i])/(b0))   #每一个都离散成b个点
        #print("px=",px)
        #print("h0=",h0)
        #print("k0=",k0) #第一个k值是对的，第二个k值不是对的
        x0[0] = X[i]
        y0[0] = Y[i]
        for j in range(1,b0):
            x0[j] = x0[j-1] + h0
            y0[j] = y0[j-1] + k0 * (x0[j] - x0[j-1])
        #将增加的点添加到数组内
        for k in range(1,b0):
            X = np.insert(X,i+k,x0[k])
            Y = np.insert(Y,i+k,y0[k])
        a = a + 49


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
    F[i+1] = s    #是i+1不是i
    #print(X[i],Y[i])
    #if(X[i+1]<X[i])
#------积分部分-----------



print("加点前点数：",len(pressure),"加点后点数：",len(X))
#plt.scatter(X0,Y0,c='r')
plt.xlabel("x / in")
plt.ylabel("dp / p")
plt.plot(X,Y,'-o',c='b')
plt.show()
#1.1将补充的点插入原有数组



'''
#积分图像作图
plt.plot(X,F,'-o')
plt.show()

'''

