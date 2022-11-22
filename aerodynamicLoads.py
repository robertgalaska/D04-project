import numpy as np
import matplotlib.pyplot as plt
#import scipy as sp
#from scipy import interpolate

f = open("MainWing_a=0.00_v=10.00ms_1000steps.txt", "r")
lines0 = f.readlines()
f.close()
g = open("MainWing_a=10.00_v=10.00ms_1000steps.txt", "r")
lines10 = g.readlines()
g.close()

rho=1.225
v=10
q = 0.5*rho*v**2

zerolist = np.array((0,0,0,0,0,0,0,0,0,0,0,0,0))
i = 0
for line0 in lines0[122:221]:

    values0 = line0.split("   ")

    valuelist0 = np.array(values0)

    if i == 0:
        array_values0 = np.vstack((zerolist, valuelist0))
    else:
        array_values0 = np.vstack((array_values0, valuelist0))
    i+=1

print(array_values0)

i = 0
for line10 in lines10[122:221]:

    values = line10.split("   ")

    valuelist = np.array(values)

    if i == 0:
        array_values10 = np.vstack((zerolist, valuelist))
    else:
        array_values10 = np.vstack((array_values10, valuelist))
    i+=1
print(array_values10)

locations0=[]
liftcoefficients0=[]
chords0=[]
for i in range(100):
    locations0.append(array_values0[i,1])
    liftcoefficients0.append(array_values0[i,4])
    chords0.append(array_values0[i,2])

lift0 = []
for i in range(len(locations0)):
    lift0.append(q*float(liftcoefficients0[i])*float(chords0[i]))
print(lift0)

locations10=[]
liftcoefficients10=[]
chords10=[]
for i in range(100):
    locations10.append(array_values10[i,1])
    liftcoefficients10.append(array_values10[i,4])
    chords10.append(array_values10[i,2])
    
lift10 = []
for i in range(len(locations10)):
    lift10.append(q*float(liftcoefficients10[i])*float(chords10[i]))
print(lift10)

plt.plot(locations0,lift0)
plt.plot(locations10,lift10)
plt.show()

