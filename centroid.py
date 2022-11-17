from math import tan, pi, radians, sin
import numpy as np
import matplotlib.pyplot as plt
#from constants import rootchord, tipchord, labda, halfspan
# function to calculate the location of the centroid of the wingbox
rho = float(input('Density:'))
V = 250
rootchord = 6.12 #as % of chord
tipchord = 1.22 #as % of chord
halfspan = 18.37
labda = 0.2
# The spanwise chord
def chord(rootchord, labda, halfspan, y):
    c = rootchord - rootchord*(1-labda)*(y/halfspan)
    return(c)
# x location of the centroid of a trapezoid
ttoc = float(input("Wingbox thickness to chord ratio (feasible values <0.003): "))
theta1 = 88.06
theta2 = 88.66
#localchord= chord(rootchord, labda, halfspan, 5)
#localchord =1

y = np.arange(0, halfspan, 0.0018)

localchord = chord(rootchord, labda, halfspan, y)
localt = ttoc * localchord
#print("localt", localt)
h = 0.5* localchord
a = 0.048 * localchord
b = 0.0764 * localchord
c = h/(tan(radians(theta1)))
x_c = h/3*((2*a+b)/(a+b))
#print("x_c" ,x_c)
# y location of the centroid of a trapezoid
y_c = (2*a*c+a*2+c*b+a*b+b**2)/(3*(a+b))
#print("y_c", y_c)
# assuming that the thickness of the wingbox is constant along the cross-section the centroid is in the same
# location as that of a solid trapezoid

#moment of inertia along the x_axis of a solid trapezoid
I_x_s = (h/12)*(a**3+3*a*c**2+3*a**2*c+b**3+c*b**2+a*b**2+b*c**2+2*a*b*c+b*a**2)
#print("I_x_s", I_x_s)
#Moment of inertia of the cut-out trapezoid:
a1 = a - (2*localt)
b1 = b - (2*localt)

h1 = h -(2*localt)
c1 = h1/(tan(radians(theta1)))
#print("a1", a1)
#print("b1", b1)
#print("h1", h1)
#print("c1", c1)
I_x_c = (h1/12)*(a1**3+3*a1*c1**2+3*(a1**2)*c1+b1**3+c1*b1**2+a1*b1**2+b1*c1**2+2*a1*b1*c1+b1*a1**2)
#print("I_x_c", I_x_c)
I_x = I_x_s - I_x_c
#print("I_x", I_x)


area = ((a-localt)+(b-localt))*(h-localt)/2
perimeter = (a-localt)+(b-localt)+(h-localt) * (1/sin(radians(theta1)) + 1/sin(radians(theta2)))
J = 4*area**2/(perimeter/localt)
#print("area",area)
#print("perimeter", perimeter)
#print("J", J)

plt.subplot(131)
plt.plot(y, I_x)
plt.axis([0, 18.7, 0, 0.025])
plt.title('Moment of inertia')
plt.xlabel('Span position')
plt.ylabel('Moment of inertia')

plt.subplot(133)
plt.plot(y, J)
plt.axis([0, 18.7, 0, 0.018])
plt.title('Torsional stiffness J')
plt.xlabel('Span position')
plt.ylabel('Torsional stiffness')

plt.show()

wingdata = np.genfromtxt('wingdata.txt')

l = wingdata[101:, 3]*wingdata[101:, 1] * 0.5 * rho * V**2
print(l)
V =