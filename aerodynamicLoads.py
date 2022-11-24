import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import integrate

### read the lines
f = open("MainWing_a=0.00_v=10.00ms_1000steps.txt", "r")
lines0 = f.readlines()
f.close()
g = open("MainWing_a=10.00_v=10.00ms_1000steps.txt", "r")
lines10 = g.readlines()
g.close()

### define constants
s = 135/2
rho=1.225
v=10
q = 0.5*rho*v**2
halfspan = 18.3689
CLd=1

### start of function to calculate loads
def calculate_aeroloads(lines10, rho, v, q):
    ### gather values for AoA0
    zerolist = np.array((0,0,0,0,0,0,0,0,0,0,0,0,0))
    i = 0
    for line0 in lines0[121:221]:

        values0 = line0.split("   ")

        valuelist0 = np.array(values0)

        if i == 0:
            array_values0 = np.vstack((zerolist, valuelist0))
        else:
            array_values0 = np.vstack((array_values0, valuelist0))
        i+=1
    ### gather values for AoA 10
    i = 0
    for line10 in lines10[121:221]:

        values = line10.split("   ")

        valuelist = np.array(values)

        if i == 0:
            array_values10 = np.vstack((zerolist, valuelist))
        else:
            array_values10 = np.vstack((array_values10, valuelist))
        i+=1

    ### create list with the lift coefficients according to spanwise location for AoA 0
    locations0=[]
    liftcoefficients0=[]
    dragcoefficients0=[]
    momentcoefficients0=[]
    chords0=[]
    dy0=[]
    CL0=0
    for i in range(101):
        locations0.append(float(array_values0[i,1]))
        liftcoefficients0.append(array_values0[i,4])
        dragcoefficients0.append(array_values0[i,6])
        momentcoefficients0.append(array_values0[i,7])
        chords0.append(array_values0[i,2])
        dy0.append(round(float(locations0[i])-float(locations0[i-1]),4))
        
    lift0 = []
    totlift0 = 0
    moment0=[]
    for i in range(len(locations0)):
        lift0.append(q*float(liftcoefficients0[i])*float(chords0[i]))
        totlift0 += dy0[i]*float(lift0[i])

    CL0= totlift0/(q*s)
    
    ### create list with the lift coefficients according to spanwise location for AoA 10
    locations10=[]
    liftcoefficients10=[]
    dragcoefficients10=[]
    momentcoefficients10=[]
    chords10=[]
    dy10=[]
    CL10= 0
    for i in range(101):
        locations10.append(float(array_values10[i,1]))
        liftcoefficients10.append(array_values10[i,4])
        dragcoefficients10.append(array_values10[i,6])
        momentcoefficients10.append(float(array_values10[i,7]))
        chords10.append(array_values10[i,2])
        dy10.append(round(float(locations10[i])-float(locations10[i-1]),4))

    lift10 = []
    totlift10 = 0
    for i in range(len(locations10)):
        lift10.append(q*float(liftcoefficients10[i])*float(chords10[i]))
        totlift10 += dy10[i]*float(lift10[i])

    CL10= totlift10/(q*s)
    #print(CL10)
    print(lift10, dy10)
    
    moment0 = []
    moment10 = []
    torque0 = []
    torque10 = []
    for i in range(len(locations0)):
        length = float(locations0[i])+((halfspan-float(locations0[i])/3))
        moment0.append(length * sum(lift0[i:-1]))
        moment10.append(length * sum(lift10[i:-1]))
        torque0.append(q*float(momentcoefficients0[i])*float(chords0[i]))
        torque10.append(q*float(momentcoefficients10[i])*float(chords10[i]))



    locations0 = np.array(locations0)
    locations10 =np.array(locations10)
    aero_lift0 = np.array(lift0)
    aero_lift10 = np.array(lift10)
    aero_moment0 = np.array(moment0)
    aero_moment10 = np.array(moment10)
    aero_induceddrag0 = np.array(dragcoefficients0)
    aero_induceddrag10 = np.array(dragcoefficients10)
    aero_torque0= np.array(torque0)
    aero_torque10= np.array(torque10)

    #Aero torque distribution
    T_aero_0 = np.zeros(100)
    T_areo_10 = np.zeros(100)
    for i in range(len(locations0)):
        T_aero_0 =  sp.integrate.trapezoid(aero_torque0[i:], locations0[i:])
    for i in range(len(locations0)):
        T_aero_10 =  sp.integrate.trapezoid(aero_torque10[i:], locations10[i:])

    #Calculate the distributed desired lift coefficient and the corresponding AoA
    CLd_distributed = []
    alpha_d=0
    def desired_CL(CLd):
        for i in range(100):
            CLd_y= CL0 + ((CLd-CL0)/(CL10-CL0))*(float(liftcoefficients10[i])-float(liftcoefficients0[i]))
            CLd_distributed.append(CLd_y)

        alpha_d= ((CLd-CL0)/(CL10-CL0))*np.sin(10*np.pi/180)
        return CLd_distributed, alpha_d

    CLd_distributed, alpha_d = desired_CL(CLd)
    
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Vertically stacked subplots')
    ax1.plot(locations0,lift0)
    ax1.plot(locations10,lift10)
    ax2.plot(locations0, moment0)
    ax2.plot(locations10, moment10)
    plt.show()



    return aero_lift0, aero_lift10, aero_moment0, aero_moment10, aero_induceddrag0, aero_induceddrag10, CLd_distributed, alpha_d, T_aero_0, T_aero_0

aero_lift0, aero_lift10, aero_moment0, aero_moment10, aero_induceddrag0, aero_induceddrag10, CLd_distributed, alpha_d, T_aero_0, T_aero_0= calculate_aeroloads(lines10, rho, v, q)
print(T_aero_0)

#print(CLd_distributed)
