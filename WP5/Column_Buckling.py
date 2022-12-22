import numpy as np
from deflecftion import M_x, M_2, M_minus_1, M_z_1, M_z_25, M_z_min
from centroid import I_y, corr_I_x, chord, option, y
from math import tan, pi, radians, sin, cos
from aerodynamicLoads import locations0
import matplotlib.pyplot as plt
import scipy as sp
from scipy import interpolate

#Defining different moments;  moment at load factor 1, 2.5 and -1 around the x and z axis
moment_1 = [M_x,M_z_1]
moment_25 = [M_2,M_z_25]
moment_min = [M_minus_1,M_z_min]

#defining constants:
width = 20          #[mm]
t=5                 #[mm]
K=1                 #[mm]
E= 69 *10**9        #[Pa]
halfspan = 18.37    #[m]
alpha = 10
rootchord = 6.12  # as % of chord
tipchord = 1.22  # as % of chord
labda = 0.2
theta1 = 88.06

#Locations of ribs for each design option:
if option == 1:
    points= [0,.6, 1.3 ,1.9,  2.6, 3.2,4, 4.8, 5.7, 6.5, 7.5, 8.4, 9.3, 10.5 ,11.7, 13, 14.1, 15.1, 16.2, 17.2, 17.9, halfspan]
elif option == 2:
    points= [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.2, 2.5, 2.9, 3.2, 3.6, 4, 4.4, 4.8,  5.2, 5.6, 6, 6.5, 7, 7.5, 8, 8.6, 9.1, 9.7, 10.4, 11, 11.8, 12.6, 13.2, 13.5, 14, 14.4, 14.8, 15.4, 16.1, 16.8, 17.4, 17.9, 18.2 ,halfspan]
elif option == 3:
    points = [0, 0.5, 0.9, 1.5, 2.1, 2.6, 3, 3.7, 4.2, 4.7, 5.4, 6, 6.8, 7.7, 8.4, 9.1, 9.9, 10.9, 12. , 13.2, 14.3, 15.4,16.4, 17.2, 18 , halfspan]

#determining the centroid of the stringer:
A= (t*width+t*(width-t))*10**(-6)     #[m^2]
x_bar = (t*width*width/2+t*(width-t)*t/2)/(t*width+t*(width-t))                 #[mm]
y_bar = (t*width*t/2+t*(width-t)*((width-t)/2+t))/(t*width+t*(width-t))         #[mm]

#calculating the moment of inertia of a single stringer:
I_xx= (width*(t**3)/12+ t*width*(y_bar-t/2)**2 + t*((width-t)**3)/12 + t*(width-t)*(y_bar-(t+(width-t)/2))**2) *10**(-12)       #[m]
I_yy= I_xx          #[m]
print('I_xx is', I_xx, 'm^4')

#function that calculated the normal stress in the cross section on the most critical points.
def normalstress(ixx, iyy, moments):

    #lists to append stresses
    stress_minwing = []
    stress_maxwing = []

    # looping over the 100 locations over the wing
    for i in range(100):

        y_wing = locations0[i]
        #finding the chord at the y coordinate
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
        x_left = -x_c
        x_right = h-x_c
        z_left = b/2        #note that this value is positive or negative because of a symmetrical plane
        z_right = a/2       #note that this value is positive or negative because of a symmetrical plane

        # List with the x and z points at all four critical points and other lists
        crit_points = [[x_left, z_left],[x_right, z_right], [x_right, -z_right], [x_left, -z_left]]
        local_stress = []
        stresses = []
        tension = []

        #calculating the bending stress for all four points on the cross section
        for j in range(4):
            x = crit_points[j][0]
            z = crit_points[j][1]

            #main stress formula
            stress = (moments[0][i]*z)/corr_I_x[i] + (moments[1][j]*x)/I_y[i]       #moment is numpy array, mistake

            info_stress = [stress, x, z]    #variable with the stress, x coordinate and z coordinate
            stresses.append(stress)
            local_stress.append(info_stress)

        high = stresses.index(max(stresses)) # get the index of the highest stress of the four points
        low = stresses.index(min(stresses)) # get the index of the lowest stress of the four points
        stress_maxwing.append(local_stress[high])   # appending that high stress to the maximum stress list per y coordinate
        stress_minwing.append(local_stress[low])    # appending that high stress to the maximum stress list per y coordinate

    # Plot the moments
    fig, axs = plt.subplots(2)
    axs[0].plot(locations0, moments[0])
    axs[0].set_title('Moment X [Nm]')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Moment [kNm]')
    axs[1].plot(locations0, moments[1], 'tab:orange')
    axs[1].set_title('Moment Z [Nm]')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Moment [kNm]')
    fig.tight_layout()
    plt.show()

    return stress_minwing, stress_maxwing

minstress, maxstress = normalstress(corr_I_x, I_y, moment_25)

# make new list with the tensions and compressions out of the stress lists
tension = []
compression = []
for i in range(len(maxstress)):
    tension.append(maxstress[i][0])
    compression.append(minstress[i][0])

#Buckling stress equation:
def buck_str(spacing):
    too_big=[]
    location_tb=[]
    buck_str= np.zeros(len(spacing))

    # loop over the difference in spacing of the wing box
    for i in range(1, len(buck_str)):
        L=spacing[i]-spacing[i-1]
        buck_str[i]= (K*E*I_xx*np.pi**2)/(A*L**2)

        # per location, check if the stress are higher than the allowable stress
        for j in range(len(locations0)):

            if spacing[i-1] < locations0[j]<=spacing[i] :
                if abs(float(minstress[j][0]))>=buck_str[i]:
                    too_big.append(minstress[j][0])
                    location_tb.append(locations0[j])
                    print(minstress[j][0],'at', locations0[j], 'is too large by a factor of', abs(minstress[j][0])/buck_str[i])

    return buck_str, too_big, location_tb

buck_stress1, too_big1, location_tb1 = buck_str(points)

# get the buckling stress to obtain the margin of safety
g = sp.interpolate.interp1d(points, buck_stress1, kind="next", fill_value="extrapolate")
buck_stress = g(locations0)
margin= buck_stress/abs(np.array(compression))

# plot graph with safety margin
plt.plot(locations0,margin)
plt.grid(True)
plt.title('Margin of safety for column buckling along the span')
plt.xlabel('Spanwise location [m]')
plt.ylabel('Margin of safety [-]')
plt.axis([0, 18.8, 0, 4])
plt.show()



