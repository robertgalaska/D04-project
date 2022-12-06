from math import pi
from centroid import localchord, localt,h
from deflecftion import E

k_c = 4
v = 0.33
sigma_critical = (pi **2 * k_c * E)/ (12 * (1-v**2)) * (localt/h)**2
print('The maximum critical stress is :', max(sigma_critical))
print('The minimum critical stress is :', min(sigma_critical))
print(sigma_critical)