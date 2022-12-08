from centroid import thickness,a, b, localchord, localt, y, area_crosssection
from main import shearneg, shearpos, torquepos
import matplotlib.pyplot as plt
from math import pi
hf = b
hb = a
E = 68.9*10**9
v = 0.33

aveshear = shearpos / ((hf+hb)*localt)
maxshear = 1.5 * aveshear

sheartorque = (torquepos/10000)/ (2*area_crosssection*localt)

sheartot = sheartorque + maxshear

plt.plot(y, abs(sheartot)/10**6)
plt.xlabel("Span position [m]")
plt.ylabel("Shear stress magnitude in spar [MPa]")
plt.show()


points1= [0, 2, 4, 6, 8, 10, 12, 14 , 16]
k = 9.5
a = 2

print(localchord[0])
print(hf[0])
criticalshear =(pi**2 * k * E * localt**2 / (12*(1-v**2)*hf[0]**2))

ratio = criticalshear/abs(sheartot)

plt.plot(y, criticalshear/10**6)
plt.xlabel("Span position [m]")
plt.ylabel("Critical shear stress [MPa]")
plt.show()

plt.plot(y, ratio)
plt.xlabel("Span position [m]")
plt.yticks([1 , 10 ,20, 30, 40, 500, 600, 700])
plt.axis([11,16, 0, 40])
plt.ylabel(" Critical shear stress/ Total shear [-]")
plt.show()
