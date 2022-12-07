from centroid import thickness,a, b, localchord, localt, y, area_crosssection
from main import shearneg, shearpos, torquepos
import matplotlib.pyplot as plt
hf = a
hb = b

aveshear = shearpos / ((hf+hb)*localt)
maxshear = 1.5 * aveshear

sheartorque = (torquepos/1000)/ (2*area_crosssection*localt)

sheartot = sheartorque + maxshear

plt.plot(y, sheartot/10**6)
plt.xlabel("Span position [m]")
plt.ylabel("Shear stress [MPa]")
plt.show()