import numpy as np
import scipy as sp
from scipy import integrate
import matplotlib.pyplot as plt

#add your dimensions
c_r = 6.12
span = 36.74

#fuel weight


#def wf(y):
    #return 0.0175 * c_r ** 2 - y ** 2 * 0.105 * c_r ** 2 / b ** 2
#step
n = 100
step = 0.8 * span / ( 2 * n )
# initialize z and y
ztab = []
z1tab = []
z2tab = []
ytab = []
a = 4.337
b = -398.23
c = 9141.6
d = 0
e = 0

# plot the fuckntion:
for i in range(n + 1):
    y = i * step
    z =  15.31*y ** 2 -562.7 * y+5170
    z1 = -(5.1 * y ** 3 - 281.4 * y ** 2 + 5170 *y - 31391.5)
    z2 = -(1.275 * y ** 4 - 93.8 * y ** 3 + 2585 *y ** 2 - 31391.5 * y + 141284.28)
    ytab.append(y)
    ztab.append(z)
    z1tab.append(z1)
    z2tab.append(z2)

for n in range(n + 1):
    y1 = n * step
    z4 = 1
    z5 =2
    z6 =3
    ytab.append(y)
    ztab.append(z)
    z1tab.append(z1)
    z2tab.append(z2)

plt.subplot(311)

plt.plot(ytab, ztab, color = "blue")
plt.margins(0.4,0)
plt.title('Load diagram for fuel weight')
plt.xlabel('Position from center of fuselage [m]')
plt.ylabel('Weight [N/m]')
plt.grid(1)

plt.subplot(312)

plt.plot(ytab, z1tab, color = "blue")
plt.margins(0.4,0)
plt.title('Shear force distibution')
plt.xlabel('Position from center of fuselage [m]')
plt.ylabel('Shear [N]')
plt.grid(1)

plt.subplot(313)

plt.plot(ytab, z2tab, color = "blue")
plt.margins(0.2,0)
plt.title('Bending moment distribution')
plt.xlabel('Position from center of fuselage [m]')
plt.ylabel('Bending moment [Nm]')
plt.grid(1)

plt.show()


#wing weight


#engine + nacelle weight
