import math 
import numpy as np
import matplotlib.pyplot as plt

for i in range(0,501,1):
    x = i * 0.01
    y = math.exp(x) * (x * x) / 2
    print(x,y)