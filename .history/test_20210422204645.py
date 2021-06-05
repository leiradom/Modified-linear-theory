import math
import numpy as np
import matplotlib.pyplot as plt

geolift = np.loadtxt("geolift.txt",dtype=np.float64)   #将文件写入数组
n0 = len(geolift)
#---------------定义储存的数组-------------------#
X0 = np.ones(n0)         #存储网格点的x坐标
Y0 = np.ones(n0)         #存储网格点的y坐标
Z0 = np.ones(n0)         #存储网格点的z坐标
X = np.ones(n0)          #存储旋转后的网格点的x坐标
Y = np.ones(n0)          #存储旋转后的网格点的y坐标
Z = np.ones(n0)          #存储旋转后的网格点的z坐标
X1 = np.ones(n0)         #存储投影后的网格点的x坐标
#Y1 = np.ones(n0)         #存储投影后的网格点的y坐标
#Z1 = np.ones(n0)         #存储网格点的z坐标
#存储表面力
dFx0 = np.ones(n0)         #存储网格点的x坐标
dFy0 = np.ones(n0)         #存储网格点的y坐标
dFz0 = np.ones(n0)         #存储网格点的z坐标
dFx1 = np.ones(n0)         #存储网格点的x坐标
dFy1 = np.ones(n0)         #存储网格点的y坐标
dFz1 = np.ones(n0)         #存储网格点的z坐标
L = np.ones(n0)         #存储每个网格单元产生的升力
C0 = np.zeros((n0,2))
#---------------定义储存的数组-------------------#

#--------------定义计算所需的一些参数-------------#
alpha  = 6.5797 / 57.3
miu = 30 / 57.3         #马赫角为30度
h = 10                  #投影的高度
s = 0
#--------------定义计算所需的一些参数-------------#

#--------------------读取流场数据文件--------------------#
for i in range(0,n0):
    X0[i] = geolift[i][0]
    Y0[i] = geolift[i][1]
    Z0[i] = geolift[i][2]
    dFx0[i] = geolift[i][3]
    dFy0[i] = geolift[i][4]
    dFz0[i] = geolift[i][5]

#print(max(X0))   #验证了正是第一列 最大为6.3421米
#--------------------读取流场数据文件--------------------#


'''
#------------------将飞行器旋转攻角--------------------- #
#绕机头向下旋转6.5797°
X1 = X0 * np.cos(-alpha) - Y0 * np.sin(-alpha)
Y1 = X0 * np.sin(-alpha) + Y0 * np.cos(-alpha)
Z1 = X0
#------------------将飞行器旋转攻角--------------------- #
'''

#-------------将飞行器上的点投影到一条线上-----------------#
for i in range(0,n0):
    X1[i] = X[i] + h / math.tan(miu)
#-------------将飞行器上的点投影到一条线上-----------------#

for i in range(0,n0):
    C0[i][0] = X1[i]
    C0[i][1] = dFy0[i]

C2 = C0[np.lexsort(C0[:,::-1].T)]