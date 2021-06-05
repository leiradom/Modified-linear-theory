import math
import numpy as np
import matplotlib.pyplot as plt

n0 = 5

X1 = [1,5,6,5.5,2]

for i in range(0, n0 - 1):
    for j in range(0, n0 - i - 1):
        if(X1[j] > X1[j+1]):
            X1[j],X1[j+1] = X1[j+1],X1[j]
            #dFy0[j],dFy0[j+1] = dFy0[j+1],dFy0[j]

print(X1)



