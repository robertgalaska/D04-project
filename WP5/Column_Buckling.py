import numpy as np
from deflecftion import M_x, M_2, M_minus_1, M_z_1, M_z_25, M_z_min
from centroid import I_y, corr_I_x, chord, option
from math import tan, pi, radians, sin, cos
from aerodynamicLoads import locations0
import matplotlib.pyplot as plt
from compressivestrength import stressrearspar, stressfrontspar, stressstringer


#Defining different moments
moment_1 = [M_x,M_z_1]
moment_25 = [M_2,M_z_25]
moment_min = [M_minus_1,M_z_min]

#defining constants:
width = 20      #[mm]
t=5             #[mm]
K=1/4           #[mm]
E= 69 *10**9    #[Pa]
halfspan = 18.37     #[m]
alpha = 10
rootchord = 6.12  # as % of chord
tipchord = 1.22  # as % of chord
labda = 0.2
theta1 = 88.06

#Locations of ribs:
if option == 1:
    points= [0,0.3,0.6, 0.9, 1.2, 1.5, 1.8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, halfspan]
elif option == 2:
    points= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, halfspan]
elif option == 3:
    points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, halfspan]
    #points= [0, 2, 4, 6, 9, 12, 16, halfspan]

#determining the centroid of the stringer:
A= (t*width+t*(width-t))*10**(-6)     #[m^2]
x_bar = (t*width*width/2+t*(width-t)*t/2)/(t*width+t*(width-t))                 #[mm]
y_bar = (t*width*t/2+t*(width-t)*((width-t)/2+t))/(t*width+t*(width-t))         #[mm]

#calculating the moment of inertia of a single stringer:
I_xx= (width*(t**3)/12+ t*width*(y_bar-t/2)**2 + t*((width-t)**3)/12 + t*(width-t)*(y_bar-(t+(width-t)/2))**2) *10**(-12)       #[m]
I_yy= I_xx          #[m]
print('I_xx is', I_xx, 'm^4')

def normalstress(ixx, iyy, moments):

    stress_minwing = []
    stress_maxwing = []

    for i in range(100):

        y_wing = locations0[i]
        localchord = chord(rootchord, labda, halfspan, y_wing)

        #dimensions of cross-section
        h = 0.5 * localchord
        a = 0.048 * localchord
        b = 0.0764 * localchord

        #centroid of area
        c = h / (tan(radians(theta1)))
        x_c = h / 3 * ((2 * a + b) / (a + b))
        y_c = (2 * a * c + a ** 2 + c * b + a * b + b ** 2) / (3 * (a + b))

        #finding the critical points
        x_left = x_c
        x_right = -h+x_c
        z_left = b/2        #note that this value is positive or negative because of a symmetrical plane
        z_right = a/2       #note that this value is positive or negative because of a symmetrical plane
        crit_points = [[x_left, z_left],[x_right, z_right], [x_right, -z_right], [x_left, -z_left]]

        local_stress = []
        stresses = []
        tension = []

        #calculating the bending stress
        for j in range(4):
            x = crit_points[j][0]
            z = crit_points[j][1]

            #print(moments[0][i], x, z, corr_I_x[i])
            stress = (moments[0][i]*z)/corr_I_x[i] + (moments[1][j]*x)/I_y[i]       #moment is numpy array, mistake

            info_stress = [stress, x, z]
            stresses.append(stress)
            local_stress.append(info_stress)

        high = stresses.index(max(stresses))
        low = stresses.index(min(stresses))

        stress_maxwing.append(local_stress[high])
        stress_minwing.append(local_stress[low])

    fig, axs = plt.subplots(2)
    # first plot: torque
    axs[0].plot(locations0, moments[0])
    axs[0].set_title('Moment X [Nm]')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Moment [kNm]')
    # second plot: bending moment
    axs[1].plot(locations0, moments[1], 'tab:orange')
    axs[1].set_title('Moment Z [Nm]')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Moment [kNm]')
    fig.tight_layout()
    plt.show()

    return stress_minwing, stress_maxwing

minstress, maxstress = normalstress(corr_I_x, I_y, moment_1)


tension = []
compression = []
for i in range(len(maxstress)):
    tension.append(maxstress[i][0])
    compression.append(minstress[i][0])



print(maxstress)
print(minstress)
print(min(tension))

#print(buck_str(points1))

#Buckling stress equation:
def buck_str(spacing):
    too_big=[]
    location_tb=[]
    buck_str= np.zeros(len(spacing))
    for i in range(1, len(buck_str)):
        L=spacing[i]-spacing[i-1]
        buck_str[i]= (K*E*I_xx*np.pi**2)/(A*L**2)

        for j in range(len(locations0)):

            if locations0[j]<=spacing[i] and locations0[j]>spacing[i-1]:
                if abs(float(minstress[j][0]))>=buck_str[i]:
                    too_big.append(minstress[j][0])
                    location_tb.append(locations0[j])
                    print(minstress[j][0],'at', locations0[j], 'is too large by a factor of', abs(minstress[j][0])/buck_str[i])
    buck_str= buck_str[1:]

    return buck_str, too_big, location_tb
buck_stress1, too_big1, location_tb1 = buck_str(points)
#print(too_big, 'are too large')
#print('at', location_tb)





