# Calculating the wing skin
from centroid import corr_I_x_s, corr_I_x_c, area, corr_I_x, Ix_frontspar, Ix_rearspar, localchord, localt, a, b, I_s
import numpy as np
from scipy import pi
from deflecftion import M_x
import matplotlib.pyplot as plt

y  = np.linspace(0.01, 18.37, 100)
l = 18.37
areafrontspar = a * localt
arearearspar = b * localt
areastringer = 0.02 * 0.005 + 0.015 * 0.005
c = 0.25
e = 68.9 * 10 ** 9
stressfrontspar = c * pi ** 2 * e * Ix_frontspar/ (l ** 2  *  areafrontspar)
stressrearspar = c * pi ** 2 * e * Ix_rearspar/ (l ** 2  * arearearspar )
stressstringer = c * pi ** 2 * e * I_s/ (l ** 2  * areastringer )

plt.subplot(311)
plt.plot(y, stressstringer)
plt.axis([0, 18.8, 0, max(stressstringer)])
plt.xticks([0,10,18.37])
plt.title('stress stringer')
plt.xlabel('..')
plt.ylabel('..')

plt.subplot(312)
plt.plot(y, stressfrontspar)
plt.axis([0, 18.8, 0, max(stressfrontspar)])
plt.xticks([0,10,18.37])
plt.title('stress frontspar')
plt.xlabel('..')
plt.ylabel('..')

plt.subplot(313)
plt.plot(y, stressrearspar)
plt.axis([0, 18.8, 0, max(stressrearspar)])
plt.xticks([0,10,18.37])
plt.title('stress rearspar')
plt.xlabel('..')
plt.ylabel('..')

plt.show()


#print(stressfrontspar)
#print(stressrearspar)
#print(stressstringer)





