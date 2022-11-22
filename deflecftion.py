# in order to calculate the deflection intergation has to be performed
import numpy as np
import matplotlib.pyplot as plt

M_x = []
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

Theta = np.ones(1000)
print(T)
for i in range(0,1000):
    T_int = T_integrand(T[:i],G,J[:i])
    Theta[i] = sp.integrate.trapezoid(y[:i],T_int)

print(len(Theta))



from centroid import halfspan
# in order to integrate this we define a new function for scipy to intergrate

def integrand_bending ():
    int = M_x/(E*I_x)
    return int
#print(integrand_bending()[0])
#sp.integrate.trapezoid(integrand_bending(), , 0.0018)

