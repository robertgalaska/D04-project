import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib.pyplot as plt

#wing dimensions
c_r = 6.12
b = 36.74

#fuel weight


#def wf(y):
    #return 0.0175 * c_r ** 2 - y ** 2 * 0.105 * c_r ** 2 / b ** 2
#step
n = 1000
step = b / ( 2 * n )
# initialize z and y
y0 = 0.0175 * c_r ** 2
ztab = []
ytab = []
a = 0.105 * c_r ** 2 / b ** 2
for i in range(n + 1):
    y = i * step
    z = y0 - a * y

    ytab.append(y)
    ztab.append(z)

plt.plot(ytab, ztab)
plt.show()
#wing weight


#engine + nacelle weight




