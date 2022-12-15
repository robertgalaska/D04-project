# Calculating the wing skin
from centroid import corr_I_x_s, corr_I_x_c, area, corr_I_x, Ix_frontspar, Ix_rearspar, localchord, localt, a, b, I_s, I_xx_s
import numpy as np
from scipy import pi
from deflecftion import M_x
import matplotlib.pyplot as plt
from Column_Buckling import points

y  = np.linspace(0.01, 18.37, 100)
l = 18.37
areafrontspar = a * localt
arearearspar = b * localt
areastringer = 0.02 * 0.005 + 0.015 * 0.005
c = 0.25
e = 68.9 * 10 ** 9
stressfrontspar = c * pi ** 2 * e * Ix_frontspar/ (l ** 2  *  areafrontspar)
stressrearspar = c * pi ** 2 * e * Ix_rearspar/ (l ** 2  * arearearspar )
stressstringer = c * pi ** 2 * e * (I_xx_s)/ (l ** 2  * areastringer )

stress_max = 276000000 # in [Pa]
mos_rearspar = stress_max / stressrearspar
mos_frontspar = stress_max / stressfrontspar
mos_stringer = stress_max / stressstringer

fig, axs = plt.subplots(3)

axs[0].plot(y, stressrearspar)
axs[0].set_title('Compressive stress in the rearspar')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('Stress [Pa]')

axs[1].plot(y, stressfrontspar, 'tab:orange')
axs[1].set_title('Compressive stress in the frontspar')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('Stress [Pa]')
fig.tight_layout()

axs[2].plot(y, stressstringer, 'tab:green')
axs[2].set_title('Compressive stress in the stringer')
axs[2].set_xlabel('Spanwise location [m]')
axs[2].set_ylabel('Stress [Pa]')
fig.tight_layout()

plt.show()

#plot for margin of safety
fig, axs = plt.subplots(3)

axs[0].plot(y, mos_rearspar)
axs[0].set_title('Margin of safety for the rearspan')
axs[0].set_xlabel('Spanwise location [m]')
axs[0].set_ylabel('Margin of safety [-]')

axs[1].plot(y, mos_frontspar, 'tab:orange')
axs[1].set_title('Margin of safety for the frontspar')
axs[1].set_xlabel('Spanwise location [m]')
axs[1].set_ylabel('Margin of safety [-]')
fig.tight_layout()

axs[2].plot(y, mos_stringer, 'tab:green')
axs[2].set_title('Margin of safety for the stringer')
axs[2].set_xlabel('Spanwise location [m]')
axs[2].set_ylabel('Margin of safety [-]')
fig.tight_layout()

plt.show()

print('min stress front spar is ', min(stressfrontspar))
print('min stress rear spar is ',min(stressrearspar))
print('min stress stringer is ',min(stressstringer))

print('max stress front spar is ', max(stressfrontspar))
print('max stress rear spar is ',max(stressrearspar))
print('max stress stringer is ',max(stressstringer))

print('Minimum factor of safety for front spar is', min(mos_frontspar))
print('Minimum factor of safety for rear spar is', min(mos_rearspar))
print('Minimum factor of safety for stringer is', min(mos_stringer))




