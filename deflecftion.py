# in order to calculate the deflection integration has to be performed
import numpy as np
import matplotlib.pyplot as plt


E= 68.9*10**9
G=26*10**9
from centroid import I_x, y, J
import scipy as sp
from scipy import integrate


#Torque deflection:
def T_integrand(T,G,J):
    int = T/(G*J)
    return int

from engine import x
T = x[0]

Theta = np.ones(100)

for i in range(0,100):
    T_int = T_integrand(T[:i],G,J[:i])
    Theta[i] = sp.integrate.trapezoid(T_int,y[:i])


plt.plot(y, Theta)
#plt.axis([0, 18.7, 0, 0.018])
plt.title('Twist distribution')
plt.xlabel('Span position')
plt.ylabel('Angle of twist')

plt.show()



from centroid import halfspan
# in order to integrate this we define a new function for scipy to integrate
from inertial_loads import z2tab
from inertial_loads import mtab
from engine import engine_bending
M_engine = engine_bending
m_tot = mtab[:100]
M_x = M_engine + m_tot
def integrand_bending (M_x,E,I_x):
    int = -M_x/(E*I_x)
    return int


slope = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_x[:i],E,I_x[:i])
    slope[i] = sp.integrate.trapezoid(y[:i],M_int)

#print(len(slope))
#print(slope)

plt.plot(y,slope)
plt.title('slope distribution')
plt.xlabel('Span position')
plt.ylabel('slope of the wing')

plt.show()

# deflection calculations
deflection = np.ones(100)
for i in range(0,100):
    deflect_int = slope[:i]
    deflection[i] = sp.integrate.trapezoid(deflect_int,y[:i])

plt.plot(y,deflection)
plt.title('deflection distribution')
plt.xlabel('Span position')
plt.ylabel('deflection of the wing')

plt.show()
