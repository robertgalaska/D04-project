from centroid import thickness,a, b, localchord, localt, y, area_crosssection
from main import shearneg, shearpos, torquepos
import matplotlib.pyplot as plt
from math import pi

# Defining basic constants
hf = b      # Height of the front spar
hb = a      # Height of the back spar
E = 68.9*10**9 # Young's Modulus
v = 0.33 # poisson's ratio

#Calculating the shear including the margin
aveshear = shearpos / ((hf+hb)*localt)
maxshear = 1.5 * aveshear
sheartorque = (torquepos/10000)/ (2*area_crosssection*localt)
sheartot = sheartorque + maxshear

#Plot figure
plt.plot(y, abs(sheartot)/10**6)
plt.xlabel("Span position [m]")
plt.ylabel("Shear stress magnitude in spar [MPa]")
plt.show()

k = 9.5     # constant for clamped thin plate, high aspact ratio from shear buckling formula
criticalshear =(pi**2 * k * E * localt**2 / (12*(1-v**2)*hf[0]**2))
ratio = criticalshear/abs(sheartot)

# Plot critical shear
plt.plot(y, criticalshear/10**6)
plt.xlabel("Span position [m]")
plt.ylabel("Critical shear stress [MPa]")
plt.show()

# Plot ratio
plt.plot(y, ratio)
plt.xlabel("Span position [m]")
plt.yticks([1 , 100 ,200, 300, 400, 500, 600])
plt.axis([0, 19, 1,600])
plt.ylabel(" Critical shear stress/ Total shear [-]")
plt.show()
