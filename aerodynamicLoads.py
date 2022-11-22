import numpy as np
import matplotlib.pyplot as plt
#import scipy as sp
#from scipy import interpolate

f = open("MainWing-a=0.00-v=10.00ms-1000steps.txt", "r")
lines0 = f.readlines()
f.close()
g = open("MainWing-a=10.00-v=10.00ms-1000steps.txt", "r")
lines10 = g.readlines()
g.close()

rho=1.225
v=10
q = 0.5*rho*v**2
halfspan = 18.3689

def calculate_aeroloads(lines10, rho, v, q):
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

    i = 0
    for line10 in lines10[122:221]:

        values = line10.split("   ")

        valuelist = np.array(values)

        if i == 0:
            array_values10 = np.vstack((zerolist, valuelist))
        else:
            array_values10 = np.vstack((array_values10, valuelist))
        i+=1

    locations0=[]
    liftcoefficients0=[]
    dragcoefficients0=[]
    chords0=[]
    for i in range(100):
        locations0.append(array_values0[i,1])
        liftcoefficients0.append(array_values0[i,4])
        dragcoefficients0.append(array_values0[i,6])
        chords0.append(array_values0[i,2])

    lift0 = []
    moment0=[]
    for i in range(len(locations0)):
        lift0.append(q*float(liftcoefficients0[i])*float(chords0[i]))

    locations10=[]
    liftcoefficients10=[]
    dragcoefficients10=[]
    chords10=[]
    for i in range(100):
        locations10.append(array_values10[i,1])
        liftcoefficients10.append(array_values10[i,4])
        dragcoefficients10.append(array_values0[i,6])
        chords10.append(array_values10[i,2])

    lift10 = []
    for i in range(len(locations10)):
        lift10.append(q*float(liftcoefficients10[i])*float(chords10[i]))

    moment0 = []
    moment10 = []
    for i in range(len(locations0)):
        length = float(locations0[i])+((halfspan-float(locations0[i])/3))
        moment0.append(length * sum(lift0[i:-1]))
        moment10.append(length * sum(lift10[i:-1]))


    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    ax1.plot(locations0,lift0)
    ax1.plot(locations10,lift10)
    ax2.plot(locations0, moment0)
    ax2.plot(locations10, moment10)
    plt.show()

    aero_lift0 = np.array(lift0)
    aero_lift10 = np.array(lift10)
    aero_moment0 = np.array(moment0)
    aero_moment10 = np.array(moment10)
    aero_induceddrag0 = np.array(dragcoefficients0)
    aero_induceddrag10 = np.array(dragcoefficients10)


    return aero_lift0, aero_lift10, aero_moment0, aero_moment10, aero_induceddrag0, aero_induceddrag10 

aero_lift0, aero_lift10, aero_moment0, aero_moment10, aero_induceddrag0, aero_induceddrag10 = calculate_aeroloads(lines10, rho, v, q)

