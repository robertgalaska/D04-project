from math import pi
from centroid import localt,h, y, n, A, halfspan
from deflecftion import E
from matplotlib import pyplot as plt
import scipy as sp
from scipy import interpolate
import numpy as np
from Column_Buckling import maxstress
a = np.array(maxstress)
b = a[:,:1]
max_stress = np.ones(100)
for i in range(100):
    max_stress[i] = (b[i])
print(max_stress)



points = [0, 3, 6, 9, 12, 15]
nofribs = [3, 2, 1, 1, 1, 1]
# nofstringers = [75, 62, 50, 40, 30, 25, 20]
f = sp.interpolate.interp1d(points, nofribs, kind="previous", fill_value="extrapolate")
ribs = f(y)
a = 3/ribs
a_b = a/(h/(n+1))

points = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 2]
k_c = [18, 14, 12, 10, 8, 6, 4.5, 4]
g = sp.interpolate.interp1d(points, k_c, kind="previous", fill_value="extrapolate")
local_k_c = g(a_b)

#k_c = 4
v = 0.33
sigma_critical = (pi **2 * local_k_c * E)/ (12 * (1-v**2)) * (localt/(h))**2
print('The maximum critical stress is :', max(sigma_critical))
print('The minimum critical stress is :', min(sigma_critical))
#print(sigma_critical)

area = n * A + localt * h
margin_of_safety = sigma_critical/((abs(max_stress)/(area))*(h/(n+1)*localt))
#margin_of_safety = sigma_critical/(abs(max_stress))
margin_of_safety[margin_of_safety>5000] = 5000
#print(margin_of_safety)
#print(normal)
#print(sigma_critical)
print('the minimum margin of safety is', min(margin_of_safety),'and is located at', (margin_of_safety.argmin())*halfspan*1/100)
fig, axs = plt.subplots(2)
axs[0].plot(y, sigma_critical)
axs[0].set_title('critical stress for skin buckling')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('stress [Pa]')
axs[1].plot(y, max_stress)
axs[1].set_title('normal stress distribution')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('applied stress [Pa]')
fig.tight_layout()
plt.show()
plt.plot(y, margin_of_safety)
plt.title('margin of safety along the span')
plt.xlabel('Spanwise location [m]')
plt.ylabel('margin of safety')
plt.show()
plt.plot(y, max_stress)
plt.title('Normal stress along the span')
plt.xlabel('Spanwise location [m]')
plt.ylabel('Applied stress [Pa]')
plt.show()