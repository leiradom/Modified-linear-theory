#多段锥的解析式

import math
import numpy as np
import matplotlib.pyplot as plt
n = 700
xi = 0.0e0
h = 4e0 / n
pi = math.pi
L = 2   #inch
M = 1.41  #输入马赫数
beta = math.sqrt(M * M - 1)
S0 = np.ones(701)
x = np.ones(701)

for i in range(0,701):
    xi = 0 + h*i
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

#判断截面的轴向位置并求解相应的截面积
    if(x11 <= 0.25 * L):
        #截面全部在圆锥上
        S = pi * a1 * b1
    elif((x11 > 0.25 * L) and (x12 < 0.25 * L)):
        rc = (0.25 * L - xi) / beta #距离轴线的距离
        if(rc > 0):
            theta = 2 * math.acos(rc / Ry1)
            Sy = 0.5 * Ry1 * Ry1 * theta - rc * math.sqrt(Ry1**2 - rc**2) #圆柱投影的弓形面积，syS圆
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
                St = 0.5 * a1**2 * theta - (Rm - rc) * math.sqrt(a1**2 - (rc- Rm)**2)
        elif(rc == 0): #圆柱投影部分为圆
            Sy =0.5 * pi * Ry1 * Ry1
            #小于1/2圆锥截面积的投影面积面积
            Rm = 0.5 * (r11 - r12)
            theta = 2 * math.acos((Rm - rc) / a1)
            St = 0.5 * a1 * a1 * theta - (Rm - rc) * math.sqrt(a1 * a1 - (rc - Rm)**2)
        elif(rc < 0):
            #圆柱投影部分面积大于半圆
            rc1 = abs(rc)
            theta = 2 * math.acos(rc1 / Ry1)
            Sy = 0.5 * Ry1**2 * theta - rc1 * math.sqrt(Ry1**2 - rc1**2)
            Sy = pi * Ry1 * Ry1  - Sy
            #小于1/2的圆锥面积的投影面积
            Rm = 0.5 *(r11 - r12)
            theta = 2 * math.acos((Rm - rc) / a1)
            St = 0.5 * a1**2 * theta - (Rm -rc) * math.sqrt(a1**2 - (Rm -rc)**2)
        S = Sy + St
    elif(xi < 0.75 * L + beta * 0.25 * L * math.sqrt(0.08 / pi)):
        #位于第一段圆柱上
        S = pi * Ry1**2

    elif(xi < 0.75 * L + beta * 0.25 * L * math.sqrt(0.08 / pi)):
        #第一段圆柱和第二段圆锥上
        rc = (0.75 * L -xi) / beta
        if(rc > 0):
            theta = 2 * math.acos(rc / Ry1)
            Sy = 0.5 * Ry1**2 * theta - rc * math.sqrt(Ry1**2 - rc**2)
            Sy = pi * Ry1**2 - Sy
            #圆锥部分截面在沿轴线方向上的投影
            Rm = 0.5 * (r21 - r22)
            if(rc > Rm):
                #小于1/2圆锥面积的投影面积
                theta = 2 * math.acos((rc - Rm) / a2)
                St = 0.5 * a2**2 * theta -(rc - Rm) * math.sqrt(a2**2 - (rc -Rm)**2)
            elif(rc == Rm):
                #等于1/2圆锥面积的投影面积
                St = 0.5 * pi * a2 * b2
            elif(rc < Rm):
                #大于1/2圆锥面积的投影面积
                theta = 2 * math.acos((Rm - rc) / a2)
                St = 0.5 * a2**2 * theta - (Rm -rc) * math.sqrt(a2**2 - (rc - Rm)**2)
                St = pi * a2 * b2 - St

        elif(rc == 0):
            #圆柱部分投影为半圆
            Sy = 0.5 * pi * Ry1**2
            #圆锥部分截面投影为大于1/2
            Rm = 0.5 * (r21 - r22)
            theta = 2 * math.acos(Rm / a2)
            St = 0.5 * theta * a2 * a2 - (Rm-rc) * math.sqrt(a2**2 - (Rm - rc)**2)
            St = pi * a2 * b2 - St
        else:
            #圆柱部分小于1/2圆
            theta = 2 * math.acos(-rc / Ry1)
            Sy = 0.5 * theta * Ry1**2 - (-rc) * math.sqrt(Ry1**2 - rc**2)
            #圆锥部分投影大于1/2**
            Rm = 0.5 * (r21 - r22)
            theta = 2 * math.acos((Rm - rc) / a2)
            St = 0.5 * theta * a2**2 - (Rm - rc) * math.sqrt(a2*a2-(Rm-rc)**2)
            St = pi * a2 * b2 - St
        S = Sy + St

#全是圆锥部分
    elif((x22>=0.75*L) and (x21<=L)):
        S = pi * a2 * b2

    elif((x21 > L) and (x22 < L)):
        rc = (L - xi) / beta
        if(rc > 0):
            theta = 2 * math.acos(rc / Ry2)
            Sy = 0.5 * Ry2**2 * theta - rc * math.sqrt(Ry2**2 - rc**2) #圆柱投影的弓形面积
            #圆锥部分截面在沿轴线方向上的投影
            Rm = 0.5 * (r21 - r22)
            if(rc > Rm):
                #大于1/2圆锥截面积的投影
                theta = 2 * math.acos((rc - Rm) / a2)
                St = 0.5 * a2**2 * theta - (rc - Rm) * math.sqrt(a2**2 - (rc - Rm)**2)
                St = pi * a2 * b2 -St
            elif(rc == Rm):
                St = 0.5 * pi * a2 * b2
            elif(rc < Rm):
                theta = 2 * math.acos((Rm -rc) / a2)
                St = 0.5 * a2**2 * theta - (Rm - rc) * math.sqrt(a2**2 - (rc - Rm)**2)
        elif(rc == 0):
            #圆柱投影部分为半圆
            Sy = 0.5 * pi * Ry2**2
            #小于1/2的圆锥截面积的投影面积
            Rm = 0.5 * (r21 - r22)
            theta = 2 * math.acos((Rm - rc) / a2)
            St = 0.5 * a2**2 * theta - (Rm - rc) * math.sqrt(a2**2 - (rc - Rm)**2)
        elif(rc < 0):
            #圆柱投影部分大于半圆
            rc1 = abs(rc)
            theta = 2 * math.acos(rc1 / Ry2)
            Sy = 0.5 * Ry2**2 * theta - rc1 * math.sqrt(Ry2**2 - rc1**2)
            Sy = pi * Ry2**2 - Sy
            #小于1/2的圆锥截面积的投影面积
            Rm = 0.5 * (r21 - r22)
            theta = 2 * math.acos((Rm - rc) / a2)
            St = 0.5 * a2**2 * theta - (Rm -rc) * math.sqrt(a2**2 - (Rm - rc)**2)
        S = Sy + St

    elif(x22 >= L):
        S = pi * Ry2**2

    x[i] = xi
    S0[i] = S
    print(xi , S)


plt.plot(x,S0)
plt.show()




