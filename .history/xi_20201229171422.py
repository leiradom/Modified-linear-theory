import math 
import numpy as np

a = np.ones([2,100])

with open('CQ.dat','w') as f1:
    for i in range(100):
        f1.write(f'{a[0][i]} {a[1][i]} \n')   #f执行大括号里面的函数