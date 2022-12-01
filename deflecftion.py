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
from aerodynamicLoads import T_aero_0, T_aero_10
T = np.add (engine_torque,T_aero_0)

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
from aerodynamicLoads import aero_moment_0
from aerodynamicLoads import aero_moment_10
M_engine = engine_bending
m_tot = inertial_moment[:100]
M_x = M_engine + inertial_moment + aero_moment_0

#print(M_engine[0])
#print(aero_moment0[0])
#print(M_0[0])
M_10 = M_engine + inertial_moment + aero_moment_10
print(M_10[0])
def integrand_bending (M_x,E,I_x):
    int = -M_x/(E*I_x)
    return int


slope = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_x[:i],E,I_x[:i])
    slope[i] = sp.integrate.trapezoid(M_int, y[:i],)

slope_10 = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_10[:i],E,I_x[:i])
    slope_10[i] = sp.integrate.trapezoid(M_int, y[:i],)

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

deflection_10 = np.ones(100)
for i in range(0,100):
    deflect_int = slope_10[:i]
    deflection_10[i] = sp.integrate.trapezoid(deflect_int,y[:i])

fig, axs = plt.subplots(2)
# first plot: deflection at aoa 0
axs[0].plot(y, deflection)
axs[0].set_title('Deflection at angle of attack at 0 deg [m]')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('Deflection [m]')
# second plot: deflection at aoa 10
axs[1].plot(y, deflection_10, 'tab:orange')
axs[1].set_title('Deflection at angle of attack at 10 deg [m]')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('Deflection [m]')
fig.tight_layout()
plt.show()

plt.show()

# Stress calculations:
#normal:
ymax = y_c
normal = M_x * ymax/I_x
print("The maximum normal stress at aoa 0 is: ", max(normal))
normal_10 = M_10 *ymax/I_x
print("The maximum normal stress at aoa 10 is: ", max(normal_10))

#shear due to torque:
sheart = engine_torque/(2*localt*area)

from inertial_loads import inertial_shear
#shear due to shear:
v = inertial_shear
shears = v*Q/(localt*I_x)

shear = shears + sheart
print("The maximum shear stress is: ", max(shear))

