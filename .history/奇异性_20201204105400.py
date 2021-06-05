import math
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(1,4.99,1000)
y = 1 / np.sqrt(5-x)
plt.plot(x,y)
plt.show()
