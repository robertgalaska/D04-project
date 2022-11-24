# in order to calculate the deflection integration has to be performed
import numpy as np
import matplotlib.pyplot as plt


E= 68.9*10**9
G=26*10**9
from centroid import I_x, y, J, localchord, y_c, localt, area, Q
import scipy as sp
from scipy import integrate


#Torque deflection:
def T_integrand(T,G,J):
    int = T/(G*J)
    return int

from engine import engine_torque
T = engine_torque

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

from inertial_loads import inertial_moment
from engine import engine_bending
from aerodynamicLoads import aero_moment0
from inertial_loads import inertial_moment_no_fuel
M_engine = engine_bending
m_tot = inertial_moment[:100]
M_x = M_engine + inertial_moment_no_fuel + aero_moment0
print(M_engine[0])
print(inertial_moment_no_fuel[0])
print(aero_moment0[0])
print(M_x[0])
def integrand_bending (M_x,E,I_x):
    int = -M_x/(E*I_x)
    return int


slope = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_x[:i],E,I_x[:i])
    slope[i] = sp.integrate.trapezoid(M_int, y[:i],)

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

# Stress calculations:
#normal:
ymax = localchord * y_c
normal = M_x * ymax/I_x
print("The maximum normal stress is: ", max(normal))

#shear due to torque:
sheart = engine_torque/(2*localt*area)

#shear due to shear:
v = 1
shears = v*Q/(localt*I_x)

shear = shears + sheart
print("The maximum shear stress is: ", max(shear))

