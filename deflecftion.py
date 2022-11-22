# in order to calcuolate the deflection intergation has to be performed
M_x = []
E = 68.9*10**9
G=26*10**9
from centroid import I_x
from
import scipy as sp
from scipy import integrate


#Torque deflection:
def T_integrand(T,G,J):
    int = T/(G*J)
    return int

from engine import x
T = x[1]

print(T)
#T_int = T_integrand(T,G,J)
Theta = sp.integrate.trapezoid(y,T,0.0018,)



from centroid import halfspan
# in order to integrate this we define a new function for scipy to intergrate

def integrand_bending ():
    int = M_x/(E*I_x)
    return int
#print(integrand_bending()[0])
#sp.integrate.trapezoid(integrand_bending(), , 0.0018)

