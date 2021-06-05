#多段锥

import math
import numpy as np
import matplotlib.pyplot as plt
n = 700
xi = 0.0e0
h = 4e0 / n
pi = math.pi
L = 1   #inch
M = 1.26  #输入马赫数
beta = math.sqrt(M * M - 1)

#第一段圆锥的部分
x11 = xi / (1 - beta * math.sqrt(0.08 / pi))
r11 = x11 * math.sqrt(0.08 / pi)
x12 = xi / (1 + beta * math.sqrt(0.08 / pi))
r12 = x12 * math.sqrt(0.08 / pi)
a1 = 0.5 * (r11 + r12)                             #椭圆长轴
b1 = 0.5 * (x11 + x12) * math.sqrt(0.08 / pi) #椭圆短轴，实际上a=b

#第二段圆锥的部分
k = (math.sqrt(2.0) - 1) * math.sqrt(0.08 / pi)
c = k * (-0.75 * L) + 0.25 * L * math.sqrt(0.08 / pi)
x21 = (xi + beta * c) / (1 - beta * k)
r21 = (x21 - xi) / beta
x22 = (xi - beta * c) / (1 + beta * k)
r22 = -(x22 - xi) / beta
a2 = 0.5 * (r21 + r22)
b2 = 0.5 * (x21 + x22) * k + c

#圆柱段的界面圆半径
Ry1 = 0.25 * L * math.sqrt(0.08 / pi)
Ry2 = L * math.sqrt(0.01 / pi)


#----------------------------------------
S0 = np.ones(701)
x = np.ones(701)



for i in range(0,701):


    if(x11 <= 0.25 * L):
        #截面全部在圆锥上
        S = pi * a1 * b1
    elif((x11 > 0.25 * L) and (x12 < 0.25 * L)):
        rc = (0.25 * L - xi) / beta #距离轴线的距离
        if(rc > 0):
            theta = 2 * math.acos(rc / Ry1)
            Sy = 0.5 * Ry1 * Ry1 * theta - rc * math.sqrt(Ry1**2 - rc**2) #圆柱投影的弓形面积，sy为syuan
            Rm = 0.5 * (r11 - r12)
            if(rc > Rm):
                #大于1/2圆锥截面积的投影面积
                theta = 2 * math.acos((rc - Rm) / a1)
                St = 0.5 * a1**2 * theta - (rc - Rm) * math.sqrt(a1**2 - (rc - Rm)**2)
                St = pi * a1 * b1 - St
            elif(rc == Rm):
                #等于1/2圆锥截面积的投影面积
                St = 0.5 * pi * a1 * b1
            elif(rc < Rm):
                #小于1/2圆锥截面积的投影面积
                theta = 2 * math.acos((Rm - rc) / a1)
                St = 0.5 * a1**2 * theta - (Rm - rc) * sqrt(a1**2 - (rc- Rm)**2)
        elif(rc == 0): #圆柱投影部分为圆
            Sy =0.5 * pi * Ry1 * Ry1
            #小于1/2圆锥截面积的投影面积面积
            Rm = 0.5 * (r11 - r12)
            theta = 2 * math.acos((Rm - rc) / a1)
            St = 0.5 * a1 * a1 * theta - (Rm - rc) * math.sqrt(a1 * a1 - (rc - Rm)**2)
