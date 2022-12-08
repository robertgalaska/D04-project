import numpy as np
from deflecftion import M_x, M_2, M_minus_1, M_z_1, M_z_25, M_z_min
from centroid import I_y, corr_I_x, chord
from math import tan, pi, radians, sin, cos

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
points1= [0, 2, 4, 6, 9, 12, 15, halfspan]
points2= [0, 2, 4, 6, 8, 12, 16, halfspan]
points3= [0, 2, 4, 6, 9, 12, 16, halfspan]

#determining the centroid of the stringer:
A= (t*width+t*(width-t))*10**(-6)     #[m^2]
x_bar = (t*width*width/2+t*(width-t)*t/2)/(t*width+t*(width-t))                 #[mm]
y_bar = (t*width*t/2+t*(width-t)*((width-t)/2+t))/(t*width+t*(width-t))         #[mm]

#calculating the moment of inertia of a single stringer:
I_xx= (width*(t**3)/12+ t*width*(y_bar-t/2)**2 + t*((width-t)**3)/12 + t*(width-t)*(y_bar-(t+(width-t)/2))**2) *10**(-12)       #[m]
I_yy= I_xx          #[m]
print('I_xx is', I_xx, 'm^4')

#Buckling stress equation:
def buck_str(spacing):
    buck_str= np.zeros(len(spacing))
    for i in range(1, len(buck_str)):
        L=spacing[i]-spacing[i-1]
        buck_str[i]= (K*E*I_xx*np.pi**2)/(A*L**2)
    return buck_str



def normalstress(ixx, iyy, moments):

    stress_minwing = []
    stress_maxwing = []

    for i in range(1):

        y_wing = (36.74 / 2) * (i / 100)
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
        crit_points = [[x_left, z_left],[x_right, z_right], [x_right, -z_right], [x_left, -z_left]  ]

        local_stress = []
        stresses = []
        #calculating the bending stress
        for i in range(4):
            x = crit_points[i][0]
            z = crit_points[i][1]

            stress = (moments[0]*z)/corr_I_x + (moments[1]*x)/I_y       #moment is numpy array, mistake

            info_stress = [stress, x, z]
            stresses.append(stress)
            local_stress.append(info_stress)

        print(type(stresses))
        high = stresses.index(max(stresses))
        low = stresses.index(min(stresses))

        stress_maxwing.append(local_stress[high])
        stress_minwing.append(local_stress[low])

    return stress_minwing, stress_maxwing

print(normalstress(corr_I_x, I_y, moment_1))









