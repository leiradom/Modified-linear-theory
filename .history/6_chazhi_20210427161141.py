import math
import numpy as np
import matplotlib.pyplot as plt

M = 2.0
gama = 1.4
B = math.sqrt(M*M - 1)
p0 = 6893.79
con = B / (gama * p0 * M**2)



volume = np.loadtxt("tu144volume.txt",dtype=np.float64)   #存放体积分布的数据文件
a = len(volume)        #a为b的长度
#X1 = np.ones(a)     #存放x的数组

X = np.ones(a)     #存放x的数组
Y = np.ones(a)     #存放x的数组
Y1 = np.ones(a)     #存放y的数组
Y20 = np.ones(a)     #存放y的数组

for i in range(0,a):
    X[i] = volume[i][0]
    Y1[i] = volume[i][1]
    #ca = cau[i][1]

lift = np.loadtxt("lift.txt",dtype=np.float64)   #存放体积分布的数据文件
b = len(lift)
print(b)
X2 = np.ones(b)     #存放x的数组
Y2 = np.ones(b)     #存放y的数组

for i in range(0,b):
    X2[i] = lift[i][0]
    Y2[i] = lift[i][1]

for i in range(0,a):
    for j in range(0,b-1):
        if (X2[j] < X[i]) and (X2[j+1] > X[i]):
            k = ((Y2[j+1] - Y2[j]) / (X2[j+1] - X2[j]))
            Y20[i] = con * (Y2[j] + k * (X[i] - X2[j]))
        else:
            j = j + 1

with open('CQ.dat','w') as f1:
    for i in range(a):
        f1.write(f'{X[i]} {Y20[i]} \n')     #f执行大括号里面的函数


plt.plot(X,Y20,'-o')
plt.show()

