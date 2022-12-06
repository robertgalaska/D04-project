import numpy as np

#defining constants:
width = 20      #[mm]
t=5             #[mm]
K=1/4           #[mm]
E= 69 *10**9    #[Pa]
halfspan = 18.37     #[m]

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
print(buck_str(points1))
