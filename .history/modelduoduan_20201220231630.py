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

#----------------------------------------
S0 = np.ones(701)
x = np.ones(701)

for i in range(0,701):
    xi = 0 + h*i
    x1 = xi / (1 - beta * math.sqrt(0.04 / pi))
    r1 = x1 * math.sqrt(0.04 / pi)
    x2 = xi / (1 + beta * math.sqrt(0.04 / pi))
    r2 = x2 * math.sqrt(0.04/pi)
    a = 0.5 * (r1 + r2)   #椭圆长轴
    b = 0.5 * (x1 + x2) * math.sqrt(0.04 / pi)   #椭圆短轴
    if(x1 <= L):
        S = pi * a * b
    elif((x1 > L)and(x2 < L)):
        rc = (L - xi) / beta
        Ry = L * math.sqrt(0.04 / pi)
        if(rc > 0):
            theta = 2 * math.acos(rc / Ry)
            Sy = 0.5* Ry * Ry * theta-rc * math.sqrt(Ry*Ry-rc * rc)
            Rm = 0.5 * (r1 - r2)
            if(rc > Rm):
                theta = 2 * math.acos((rc - Rm)/a)
                St = 0.5 * a * a * theta - (rc-Rm) * math.sqrt(a*a-(rc-Rm)**2)  #St为St
                St = pi * a * b - St
            elif(rc==Rm):
                St = 0.5 * pi * a * b
            elif(rc < Rm):    
                theta = 2 * math.acos((Rm - rc)/a)
                St = 0.5 * a * a * theta-(Rm-rc)*math.sqrt(a*a-(rc-Rm)**2)
        elif(rc == 0):
            Sy = 0.5 * pi * Ry * Ry
            Rm = 0.5 * (r1 - r2)
            theta = 2 * math.acos((Rm-rc)/a)
            St = 0.5 * a * a * theta-(Rm-rc) * math.sqrt(a*a-(rc-Rm)**2)
        elif(rc < 0):
            rc1 = abs(rc)
            theta = 2 * math.acos(rc1/Ry)
            Sy = 0.5 * Ry * Ry * theta - rc1 * math.sqrt(Ry * Ry - rc1 * rc1)
            Sy = pi * Ry * Ry -Sy
            Rm = 0.5 * (r1 - r2)
            theta = 2 * math.acos((Rm-rc)/a)
            St = 0.5 * a * a * theta-(Rm-rc) * math.sqrt(a*a-(Rm-rc)**2)
        S = Sy + St
    else:
        Ry = L * math.sqrt(0.04 / pi)
        S=pi * Ry * Ry
    x[i] = xi
    S0[i] = S
    print(xi , S)   











