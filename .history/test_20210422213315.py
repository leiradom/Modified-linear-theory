import math
import numpy as np
import matplotlib.pyplot as plt


geolift = np.loadtxt("geolift.txt",dtype=np.float64)   #将文件写入数组
n0 = len(geolift)

#Y1 = np.ones(n0)         #存储投影后的网格点的y坐标
#Z1 = np.ones(n0)         #存储网格点的z坐标
#存储表面力
dFy0 = np.ones(n0)         #存储网格点的x坐标

for i in range(0,n0):
    dFy0[i] = geolift[i][4]


s = 0
for i in range(1,n0):
    s = s + dFy0[i]

print(2*s)
