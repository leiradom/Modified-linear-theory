import math
import numpy as np
import matplotlib.pyplot as plt

volume = np.loadtxt("tu144volume.txt",dtype=np.float64)   #存放体积分布的数据文件
lift = np.loadtxt("arealift.txt",dtype=np.float64)
a = len(lift)
X = np.zeros(a)
Y = np.zeros(a)

for i in range(0,a):
    X[i] = volume[i][0]
    Y[i] = volume[i][1] + lift[i][1]

plt.plot(X,Y)
plt.show()

with open('total.dat','w') as f1:
    for i in range(a):
        f1.write(f'{X[i]} {Y[i]} \n')     #f执行大括号里面的函数
