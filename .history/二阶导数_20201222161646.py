import math 
import numpy as np
import matplotlib.pyplot as plt


b = np.loadtxt("mode11ma126.txt",dtype=np.float64)
#print(b[1][0])
a = len(b)
print(a)           #a的值为1001
C = np.ones(a)
D = np.ones(a)
B = np.ones(a)
for i in range(0,a):
    c = b[i][0]
    d = b[i][1]
    C[i] = c
    D[i] = d
print(C)      #C是x
print(D)      #D是y

h = (C[a-1]/(a))      #计算的步长

for i in range(0,a-2):
    se = ((1 / h**2)*(D[i] - 2 * D[i+1] + D[i+2]))
    B[i] = se

for i in range(0,a-2):
    print(C[i],B[i])

plt.plot(C,B)
plt.show()

##验证算法的精确度  步长最好不要超过0.001
#for i in range(0,a-2):
#    print(C[i],(B[i]-D[i]))    #求二阶导百分之1.2的误差