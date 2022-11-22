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
n = 1000
step = 0.8 * span / ( 2 * n )
# initialize z and y
ztab = []
z1tab = []
z2tab = []

z4tab =[]
z5tab = []
z6tab = []

ytab = []
y1tab= []
y2tab = []

z7tab = []
z8tab = []
z9tab = []

wtab = []
vtab = []
mtab = []

# plot the fuckntion:
for i in range(n + 1):

    #fuel
    if i * step < 14.7:
        y = i * step
        z =  15.31*y ** 2 -562.7 * y + 5170
        z1 = -(5.1 * y ** 3 - 281.4 * y ** 2 + 5170 *y - 31391.5)
        z2 = -(1.275 * y ** 4 - 93.8 * y ** 3 + 2585 *y ** 2 - 31391.5 * y + 141284.28)
        ytab.append(y)
        ztab.append(z)
        z1tab.append(z1)
        z2tab.append(z2)

    if i * step < 18.37:
    #wing weight
        z4 = 9.65 * y ** 2 - 445.77 * y + 5147.3 
        z5 = -1 * (3.217 * y ** 3 - 222.9 * y ** 2 + 5147.3 * y - 39235.8)
        z6 = -1 * (0.804 * y ** 4 - 74.3 * y ** 3 + 2573.7 * y ** 2 - 39235.8 * y + 221283.5)
    
        z4tab.append(z4)
        z5tab.append(z5)
        z6tab.append(z6)

    if i * step < 6.43:
    #engine weight
        z7 = 0
        z8 = -34780
        z9 = -34780 * y + 224214
    
        z7tab.append(z7)
        z8tab.append(z8)
        z9tab.append(z9)

    wtab.append(z + z4 + z7)
    vtab.append(z1 + z5 + z8)
    mtab.append(z2 + z6 + z9)
    


plt.subplot(311)

plt.plot(ytab, wtab, color = "blue")
#plt.margins(0.4,0)
plt.title('Load diagram for weight')
plt.xlabel('Position from center of fuselage [m]')
plt.ylabel('Weight [N/m]')
plt.grid(1)

plt.subplot(312)

plt.plot(ytab, vtab, color = "blue")
#plt.margins(0.4,0)
plt.title('Shear force distibution')
plt.xlabel('Position from center of fuselage [m]')
plt.ylabel('Shear [N]')
plt.grid(1)

plt.subplot(313)

plt.plot(ytab, mtab, color = "blue")
#plt.margins(0.2,0)
plt.title('Bending moment distribution')
plt.xlabel('Position from center of fuselage [m]')
plt.ylabel('Bending moment [Nm]')
plt.grid(1)

plt.show()
