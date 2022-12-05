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
from aerodynamicLoads import T_aero_0, T_aero_10, aero_torque_CLd_1, aero_torque_CLd_25, aero_torque_CLd_min
T = np.add (engine_torque,aero_torque_CLd_1)
T_2 = np.add (engine_torque,aero_torque_CLd_25)
T_minus_1 = np.add (engine_torque,aero_torque_CLd_min)

Theta = np.ones(100)
for i in range(0,100):
    T_int = T_integrand(T[:i],G,J[:i])
    Theta[i] = sp.integrate.trapezoid(T_int,y[:i])

Theta_2 = np.ones(100)
for i in range(0,100):
    T_int = T_integrand(T_2[:i],G,J[:i])
    Theta_2[i] = sp.integrate.trapezoid(T_int,y[:i])

Theta_minus_1 = np.ones(100)
for i in range(0,100):
    T_int = T_integrand(T_minus_1[:i],G,J[:i])
    Theta_minus_1[i] = sp.integrate.trapezoid(T_int,y[:i])



print(Theta_2[-1])
fig, axs = plt.subplots(3)
axs[0].plot(y, Theta)
axs[0].set_title('Twist distribution at load factor 1')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('Angle of twist')
axs[1].plot(y, Theta_2, 'tab:orange')
axs[1].set_title('Twist distribution at load factor 2.5')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('Angle of twist')
axs[2].plot(y, Theta_minus_1, 'tab:green')
axs[2].set_title('Twist distribution at load factor -1')
axs[2].set_xlabel('Spanwise location [m]')
axs[2].set_ylabel('Angle of twist')
fig.tight_layout()
plt.show()
#plt.plot(y, Theta)
#plt.axis([0, 18.7, 0, 0.018])
#plt.title('Twist distribution')
#plt.xlabel('Span position')
#plt.ylabel('Angle of twist')

#plt.show()



from centroid import halfspan
# in order to integrate this we define a new function for scipy to integrate

from inertial_loads import inertial_moment
from engine import engine_bending
from aerodynamicLoads import aero_moment_0, aero_shear0
from aerodynamicLoads import aero_moment_10, aero_moment_CLd_1, aero_moment_CLd_25, aero_moment_CLd_min
M_engine = engine_bending
m_tot = inertial_moment[:100]
M_x = M_engine + inertial_moment + aero_moment_CLd_1
M_2 = M_engine + inertial_moment + aero_moment_CLd_25
M_minus_1 = M_engine + inertial_moment + aero_moment_CLd_min
#print(M_engine[0])
#print(aero_moment0[0])
#print(M_0[0])
M_10 = M_engine + inertial_moment + aero_moment_10
#print(M_10[0])
def integrand_bending (M_x,E,I_x):
    int = -M_x/(E*I_x)
    return int


slope = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_x[:i],E,I_x[:i])
    slope[i] = sp.integrate.trapezoid(M_int, y[:i],)

slope_2 = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_2[:i],E,I_x[:i])
    slope_2[i] = sp.integrate.trapezoid(M_int, y[:i],)

slope_minus_1 = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_minus_1[:i],E,I_x[:i])
    slope_minus_1[i] = sp.integrate.trapezoid(M_int, y[:i],)

slope_10 = np.ones(100)
for i in range(0,100):
    M_int = integrand_bending(M_10[:i],E,I_x[:i])
    slope_10[i] = sp.integrate.trapezoid(M_int, y[:i],)

#print(len(slope))
#print(slope)

#plt.plot(y,slope)
#plt.title('slope distribution')
#plt.xlabel('Span position')
#plt.ylabel('slope of the wing')

#plt.show()

# deflection calculations
deflection = np.ones(100)
for i in range(0,100):
    deflect_int = slope[:i]
    deflection[i] = sp.integrate.trapezoid(deflect_int,y[:i])

deflection_2 = np.ones(100)
for i in range(0,100):
    deflect_int = slope_2[:i]
    deflection_2[i] = sp.integrate.trapezoid(deflect_int,y[:i])

deflection_minus_1 = np.ones(100)
for i in range(0,100):
    deflect_int = slope_minus_1[:i]
    deflection_minus_1[i] = sp.integrate.trapezoid(deflect_int,y[:i])

deflection_10 = np.ones(100)
for i in range(0,100):
    deflect_int = slope_10[:i]
    deflection_10[i] = sp.integrate.trapezoid(deflect_int,y[:i])

fig, axs = plt.subplots(3)
# first plot: deflection at aoa 0
axs[0].plot(y, deflection)
axs[0].set_title('Deflection at load factor 1')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('Deflection [m]')
# plot of deflection at load factor 2.5
axs[1].plot(y, deflection_2, 'tab:orange')
axs[1].set_title('Deflection at load factor of 2.5')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('Deflection [m]')
# deflection at load factor -1
axs[2].plot(y, deflection_minus_1, 'tab:green')
axs[2].set_title('Deflection at load factor -1')
axs[2].set_xlabel('Spanwise location [m]')
axs[2].set_ylabel('Deflection [m]')
# second plot: deflection at aoa 10
#axs[1].plot(y, deflection_10, 'tab:orange')
#axs[1].set_title('Deflection at angle of attack at 10 deg [m]')
#axs[1].set_xlabel('Spanwise location [m]')
#axs[1].set_ylabel('Deflection [m]')
fig.tight_layout()
plt.show()

plt.show()
Twists = [Theta[-1], Theta_2[-1], Theta_minus_1[-1]]
Deflections = [deflection[-1], deflection_2[-1], deflection_minus_1[-1]]
case = [1, 2.5, -1]
print('The max twist is', max(Twists, key=abs),'. This is for load factor', case[Twists.index(max(Twists, key=abs))])
print('The max deflection is', max(Deflections, key=abs),'. This is for load factor', case[Deflections.index(max(Deflections, key = abs))])
# Stress calculations:
#normal:
ymax = y_c
normal = M_2 * ymax/I_x
print("The maximum normal stress at load factor 2.5 is : ", max(normal, key=abs))
normal_10 = M_minus_1 *ymax/I_x
print("The maximum normal stress at load factor -1 is: ", max(normal_10, key=abs))
normal_1 = M_x *ymax/I_x
print("The maximum normal stress at load factor 1 is: ", max(normal_1, key=abs))

fig, axs = plt.subplots(3)
# first plot: deflection at aoa 0
axs[0].plot(y, normal_1)
axs[0].set_title('normal stress at load factor 1')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('stress [Pa]')
# plot of deflection at load factor 2.5
axs[1].plot(y, normal, 'tab:orange')
axs[1].set_title('normal stress at load factor 2.5')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('Stress [Pa]')
axs[2].plot(y, normal_10, 'tab:green')
axs[2].set_title('normal stress at load factor -1')
axs[2].set_xlabel('Spanwise location [m]')
axs[2].set_ylabel('Stress [Pa]')
fig.tight_layout()
plt.show()


#shear due to torque:
#sheart = engine_torque/(2*localt*area)

#from inertial_loads import inertial_shear
#shear due to shear:
#v = inertial_shear + aero_shear0
#shears = v*Q/(localt*I_x)

#shear = shears + sheart
#print("The maximum shear stress is: ", max(shear))

