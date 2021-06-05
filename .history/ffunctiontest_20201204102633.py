import math
import numpy as np
import matplotlib.pyplot as plt

'''
x = np.linspace(1,10,1000)
y = np.exp(x)
plt.plot(x,y)
plt.show()
print(x,y)
'''

for i in range(0,501,1):
    x = i * 0.01
    y = 2 * x**(0.5)
    print(x,y)

for i in range(0,501,1):
    x1 = i * 0.01
    y1 = 2 * math.exp(0.5)
    print(x1,y1)

plt.plot(x,y)
plt.plot(x1,y1)
plt.show()