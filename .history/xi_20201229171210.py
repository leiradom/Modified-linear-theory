import math 
import numpy as np

a = np.ones([2,100])

with open('CQ.dat','r') as f1:
    for i in range(100):
        a = f1.readline()   #f执行大括号里面的函数

print(a)