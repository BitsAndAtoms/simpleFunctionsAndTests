import matplotlib.pyplot as plt 
import numpy as np 
from pylab import *
import statistics

t = np.arange(0,10,0.1)
a = np.sin(t) 
b = np.mean(a)
print(statistics.stdev(a))
print(b)
plt.plot(t,a)
plt.show()