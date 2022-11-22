# in order to calculate the deflection intergation has to be performed
import scipy as sp
from scipy import integrate
import numpy as np
M_x = [2]
E = 68.9*10**9
from centroid import I_x
from

from centroid import halfspan
# in order to integrate this we define a new function for scipy to intergrate

def integrand_bending ():
    int = M_x/(E*I_x)
    return int
#print(integrand_bending()[0])
sp.integrate.trapezoid(integrand_bending(), , 0.0018)

