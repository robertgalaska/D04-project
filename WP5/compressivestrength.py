# Calculating the wing skin
from centroid import I_x_s, I_x_c, area, I_x, Ix_frontspar, Ix_rearspar
import numpy as np
from deflecftion import M_x, y
a = M_x * y /(I_x_s + I_x_c)
print(M_x * y /I_x_s)

print( min (a ))

print ( 0.794 * 3.14 ** 2 * 68.9 * 10 ** 9 * I_x/ ( y ** 2 * area))





