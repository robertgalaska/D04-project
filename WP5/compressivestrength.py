# Calculating the wing skin
from centroid import corr_I_x_s, corr_I_x_c, area, corr_I_x, Ix_frontspar, Ix_rearspar, localchord, localt, a, b, I_s
import numpy as np
from scipy import pi
from deflecftion import M_x, y
import matplotlib.pyplot as plt

areafrontspar = a * localt
arearearspar = b * localt
areastringer = 0.02 * 0.005 + 0.015 * 0.005
c = 0.25
e = 68.9 * 10 ** 9
stressfrontspar = c * pi ** 2 * e * Ix_frontspar/ (y ** 2  *  areafrontspar)
stressrearspar = c * pi ** 2 * e * Ix_rearspar/ (y ** 2  * arearearspar )
stressstringer = c * pi ** 2 * e * I_s/ (y ** 2  * areastringer )


print(stressfrontspar)
print(stressrearspar)
print(stressstringer)



