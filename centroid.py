from math import tan, pi, radians, sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import interpolate, integrate



# from constants import rootchord, tipchord, labda, halfspan
# function to calculate the location of the centroid of the wingbox

alpha = 10
rootchord = 6.12  # as % of chord
tipchord = 1.22  # as % of chord
halfspan = 18.37
labda = 0.2


# The spanwise chord
def chord(rootchord, labda, halfspan, y):
    c = rootchord - rootchord * (1 - labda) * (y / halfspan)
    return (c)



# ttoc = float(input("Wingbox thickness to chord ratio (feasible values <0.003): "))
theta1 = 88.06
theta2 = 88.66
# localchord= chord(rootchord, labda, halfspan, 5)
# localchord =1

y = np.linspace(0, halfspan, 100)

localchord = chord(rootchord, labda, halfspan, y)
# localt = ttoc * localchord
option = float(input('Which design option do you want to analyze? (1 - high stringer low thickness, 2 - low stringer high thickness, 3 - intermediate) '))

if option == 1:
    points_1 = [0, 2, 4, 6, 9, 12,15]
    thickness = [0.0265, 0.024, 0.022, 0.02, 0.015, 0.010, 0.005]


    points_2 = [0,2, 4, 6, 9, 12, 15]
    nofstringers = [153, 139, 126, 113, 93, 73, 53]
elif option == 2:

    points_1 = [0, 2, 4, 6, 8, 12, 16]
    thickness = [0.04, 0.038, 0.035, 0.03, 0.023, 0.020, 0.01]


    points_2 = [0, 3, 10, 15]
    nofstringers = [4, 3, 2, 1]
elif option == 3:
    points_1 = [0, 2, 4, 6, 9, 12, 14, 16]
    thickness = [0.022, 0.021, 0.019, 0.018, 0.017, 0.016, 0.014, 0.013]

    points_2 = [0, 2, 4, 6, 9, 12, 15]
    nofstringers = [108, 104, 98, 95, 93, 73, 53]


# nofstringers = [75, 62, 50, 40, 30, 25, 20]
g = sp.interpolate.interp1d(points_1, thickness, kind="previous", fill_value="extrapolate")
localt = g(y)
f = sp.interpolate.interp1d(points_2, nofstringers, kind="previous", fill_value="extrapolate")
n = f(y)

L = 0.02
y_wingboxstringers = []

for i in points_2:
    y_chord = 0.5 * chord(rootchord, labda, halfspan, i)
    stringer_num = y_chord / L
    y_wingboxstringers.append(stringer_num)

print(y_wingboxstringers)

#relevant dimensions for the trapezoid
h = 0.5 * localchord
a = 0.048 * localchord
b = 0.0764 * localchord
c = h / (tan(radians(theta1)))
# x location of the centroid
x_c = h / 3 * ((2 * a + b) / (a + b))
# y location of the centroid of a trapezoid
y_c = (2 * a * c + a ** 2 + c * b + a * b + b ** 2) / (3 * (a + b))

# assuming that the thickness of the wingbox is constant along the cross-section the centroid is in the same
# location as that of a solid trapezoid



#relevant dimensions of the cut-out trapezoid
a1 = a - (2 * localt)
b1 = b - (2 * localt)
h1 = h - (2 * localt)
c1 = h1 / (tan(radians(theta1)))

# moment of inertia along the y_axis of a solid trapezoid:
I_y_s = (h**3*(a**2+4*a*b+b**2))/(36*(a+b))
#moment of inertia along the y axis of the cut-out trapezoid:
I_y_c = (h1**3*(a1**2+4*a1*b1+b1**2))/(36*(a1+b1))
# moment of inertia along the x_axis of a solid trapezoid:
corr_I_x_s = (h*(4*a*b*c**2+3*a**2*b*c-3*a*b**2*c+a**4+b**4+2*a**3*b+a**2*c**2+a**3*c+2*a*b**3-c*b**3+b**2*c**2))/(36*(a+b))
# Moment of inertia of the cut-out trapezoid:
corr_I_x_c = (h1*(4*a1*b1*c1**2+3*a1**2*b1*c1-3*a1*b1**2*c1+a1**4+b1**4+2*a1**3*b1+a1**2*c1**2+a1**3*c1+2*a1*b1**3-c1*b1**3+b1**2*c1**2))/(36*(a1+b1))

t = 0.005
A = t * (2 * L - t)
x_bar = (t*L*L/2+t*(L-t)*t/2)/(t*L+t*(L-t))
y_bar = (t*L*t/2+t*(L-t)*((L-t)/2+t))/(t*L+t*(L-t))



# moment of inertia increase due to stingers can be calculated by adding the steiner terms of the individual stringers
I_s = n * A * y_c ** 2 + n * A * (a - y_c) ** 2
I_s_y = n * A * x_c **2 + n * A * (h - x_c)**2
I_y = I_y_s - I_y_c

I_xx_s= n* (L*(t**3)/12+ t*L*(y_bar-t/2)**2 + t*((L-t)**3)/12 + t*(L-t)*(y_bar-(t+(L-t)/2))**2)

corr_I_x = corr_I_x_s - corr_I_x_c + I_s


#plt.subplot(131)
#plt.plot(y, I_x)
#plt.axis([0, 18.7, 0, 0.030])
#plt.xticks([0,10,18.37])
#plt.title('Moment of inertia')
#plt.xlabel('Span position[m]')
#plt.ylabel('Moment of inertia')

#plt.subplot(133)
#plt.plot(y, corr_I_x)
#plt.axis([0, 18.8, 0, 0.025])
#plt.xticks([0,10,18.37])
#plt.title('Moment of inertia calculated the correct way')
#plt.xlabel('Span position[m]')
#plt.ylabel('Moment of inertia')
#plt.show()

Ix_frontspar = (localt * b**3)/12 + localt*b*(y_c - b/2)**2
Ix_rearspar = (localt * a**3)/12 + localt*a*(y_c - a/2)**2

area = ((a - localt) + (b - localt)) * (h - localt) / 2
perimeter = (a - localt) + (b - localt) + (h - localt) * (1 / sin(radians(theta1)) + 1 / sin(radians(theta2)))
integral = 2*n * (L - t) / (t + localt) + 2*n * t / (localt + L) + (perimeter - 2* n * L) / localt
J = 4 * area ** 2 / integral


plt.subplot(131)
plt.plot(y, corr_I_x)
plt.axis([0, 18.7, 0, 0.030])
plt.xticks([0,10,18.37])
plt.title('Moment of inertia')
plt.xlabel('Span position[m]')
plt.ylabel('Moment of inertia')

plt.subplot(133)
plt.plot(y, J)
plt.axis([0, 18.8, 0, 0.025])
plt.xticks([0,10,18.37])
plt.title('Torsional stiffness J')
plt.xlabel('Span position[m]')
plt.ylabel('Torsional stiffness')

plt.show()

# Mass calculations:
area_crosssection = perimeter * localt
area_stringers = n * A
totarea = area_stringers + area_crosssection

Volume = sp.integrate.trapezoid(totarea, y)
print(Volume)
density = 2700
mass = density * Volume
print("The mass of this wingbox configuration is: ", mass)

# Q for shear calculations:
Q = 0.01964 * localchord ** 2 * localt
