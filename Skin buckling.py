from math import pi
from centroid import localchord, localt,h, y, halfspan
from deflecftion import E, normal
from matplotlib import pyplot as plt
import scipy as sp
from scipy import interpolate


a = halfspan/25
a_b = a/h

points = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 2]
k_c = [18, 14, 12, 10, 8, 6 , 4.5 , 4]
g = sp.interpolate.interp1d(points, k_c, kind="previous", fill_value="extrapolate")
local_k_c = g(a_b)

k_c = 4
v = 0.33
sigma_critical = (pi **2 * local_k_c * E)/ (12 * (1-v**2)) * (localt/h)**2
print('The maximum critical stress is :', max(sigma_critical))
print('The minimum critical stress is :', min(sigma_critical))
#print(sigma_critical)


margin_of_safety = sigma_critical/abs(normal)



fig, axs = plt.subplots(3)
axs[0].plot(y, sigma_critical)
axs[0].set_title('critical stress for skin buckling')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('stress [Pa]')
axs[1].plot(y, a_b)
axs[1].set_title('a/b')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('a/b')
axs[2].plot(y, margin_of_safety)
axs[2].set_title('margin of safety along the span')
axs[2].set_xlabel('Spanwise location [m]')
axs[2].set_ylabel('margin of safety')
fig.tight_layout()
plt.show()
print(sigma_critical[0])