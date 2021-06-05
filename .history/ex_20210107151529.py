import math
import numpy as np
import matplotlib.pyplot as plt


a = np.ones(10)
b = np.ones(10)

np.insert(a,1,10)

print(a)







'''
x = np.linspace(1,10,1000)
y = np.exp(x)
plt.plot(x,y)
plt.show()
print(x,y)
'''
'''
for i in range(0,5001,1):
    x = i * 0.001
    y = math.exp(x)
    print(x,y)
'''