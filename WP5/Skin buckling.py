from math import pi
from centroid import localt,h, y, n, A, halfspan
from deflecftion import E
from matplotlib import pyplot as plt
import scipy as sp
from scipy import interpolate
from Column_Buckling import maxstress, points
from aerodynamicLoads import locations0

# getting max stress from file Column buckling
a = np.array(maxstress)
b = a[:,:1]
max_stress = np.ones(100)
for i in range(100):
    max_stress[i] = (b[i])
print(max_stress)

#Length between the ribs calculations
points_r = points
for i in range(1, len(points_r)):
    L = points_r[i] - points_r[i - 1]

# Ratios from skin panel
a = L
a_b = a/(h/(n+1))
points = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 2]
k_c = [18, 14, 12, 10, 8, 6, 4.5, 4]
g = sp.interpolate.interp1d(points, k_c, kind="previous", fill_value="extrapolate") # approximating a curve
local_k_c = g(a_b)  # obtain the Kc out of the interpolation

v = 0.33    #poisson's ratio
sigma_critical = (pi **2 * local_k_c * E)/ (12 * (1-v**2)) * (localt/(h))**2
area = n * A + localt * h
margin_of_safety = sigma_critical/((abs(max_stress)/(area))*(h/(n+1)*localt))   # calculating margin
margin_of_safety[margin_of_safety>5000] = 5000  # define max margin

#plotting stress and margin of safety
fig, axs = plt.subplots(2)
axs[0].plot(locations0, sigma_critical)
axs[0].set_title('critical stress for skin buckling')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('stress [Pa]')
axs[1].plot(locations0, max_stress)
axs[1].set_title('normal stress distribution')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('applied stress [Pa]')
fig.tight_layout()
plt.show()
plt.plot(locations0, margin_of_safety)
plt.grid(True)
plt.title('margin of safety along the span')
plt.xlabel('Spanwise location [m]')
plt.ylabel('margin of safety')
plt.show()
plt.plot(locations0, max_stress)
plt.grid(True)
plt.title('Normal stress along the span')
plt.xlabel('Spanwise location [m]')
plt.ylabel('Applied stress [Pa]')
plt.show()
