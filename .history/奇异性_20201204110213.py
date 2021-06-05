import math
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(1,4.99,1000)
y = 1 / np.sqrt(5-x)
plt.plot(x,y)
plt.show()


#以1/x解决积分过程中的奇异性的问题
s = 0
x = np.ones(501)
for i in range(1,501):
    x[i] = 0.01 * i

for i in range(1,500):
    si = (1/x[i+1] + 1/x[i]) * ((x[i+1]-x[i])/2)
    s = si +s

print(s)