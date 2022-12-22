# Calculating the wing skin
from centroid import  Ix_frontspar, Ix_rearspar,localt, a, b, I_xx_s,y
import numpy as np
from scipy import pi
from deflecftion import M_x
import matplotlib.pyplot as plt

# Defining basic constants
l = 18.37       # half span length
areafrontspar = b * localt      #b is the length of the front spar
arearearspar = a * localt       #a is the length of the back spar
areastringer = 0.02 * 0.005 + 0.015 * 0.005
c = 0.25        # given value determined by compressive strength formula
e = 68.9 * 10 ** 9  #Young's Modulus of aluminium

#Calculating the stresses
stressfrontspar = c * pi ** 2 * e * Ix_frontspar/ (l ** 2  *  areafrontspar)
stressrearspar = c * pi ** 2 * e * Ix_rearspar/ (l ** 2  * arearearspar )
stressstringer = c * pi ** 2 * e * (I_xx_s)/ (l ** 2  * areastringer )
stress_max = 276000000 # in [Pa]

#Margin of safety calcuations
mos_rearspar = stress_max / stressrearspar
mos_frontspar = stress_max / stressfrontspar
mos_stringer = stress_max / stressstringer

# plotting the graphs of the stresses
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

