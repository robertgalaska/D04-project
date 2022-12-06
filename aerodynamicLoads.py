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
s = 135
rho=0.4416
v=256
q = 0.5*rho*v**2
halfspan = 18.3689
n = [1,2.5,-1]
W=22318.81*9.81

def calculate_Cld(n):
    Clds = []
    for i in n:
        L=(i*W)
        CLd=L/(q*s)
        Clds.append(CLd)

    return Clds[0], Clds[1], Clds[2]

Cld1, Cld2, Cld3 = calculate_Cld(n)

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
    array_values0=np.delete(array_values0, (0), axis=0)
    array_values10=np.delete(array_values10, (0), axis=0)
    
    ### create list with the lift coefficients according to spanwise location for AoA 0
    locations0=[]
    liftcoefficients0=[]
    dragcoefficients0=[]
    momentcoefficients0=[]
    chords0=[]
    dy0=[]
    CL0=0
    for i in range(100):
        locations0.append(float(array_values0[i,1]))
        liftcoefficients0.append(float(array_values0[i,4]))
        dragcoefficients0.append(float(array_values0[i,6]))
        momentcoefficients0.append(float(array_values0[i,7]))
        chords0.append(float(array_values0[i,2]))
        dy0.append(round(float(locations0[i])-float(locations0[i-1]),4))

    #calculate the total lift for AoA0        
    lift0 = []
    totlift0 = 0
    moment0=[]
    for i in range(len(locations0)):
        lift0.append(q*liftcoefficients0[i]*chords0[i])
        totlift0 += dy0[i]*lift0[i]

    CL0= totlift0/(q*s)
    
    ### create list with the lift coefficients according to spanwise location for AoA 10
    locations10=[]
    liftcoefficients10=[]
    dragcoefficients10=[]
    momentcoefficients10=[]
    chords10=[]
    dy10=[]
    CL10= 0
    for i in range(100):
        locations10.append(float(array_values10[i,1]))
        liftcoefficients10.append(float(array_values10[i,4]))
        dragcoefficients10.append(float(array_values10[i,6]))
        momentcoefficients10.append(float(array_values10[i,7]))
        chords10.append(float(array_values10[i,2]))
        dy10.append(round(locations10[i]-locations10[i-1],4))

    #calculate the total lift for AoA10
    lift10 = []
    totlift10 = 0
    for i in range(len(locations10)):
        lift10.append(q*liftcoefficients10[i]*chords10[i])
        totlift10 += dy10[i]*lift10[i]
    CL10= totlift10/(q*s)

    #shear distribution
    aero_lift0 = np.array(lift0)
    aero_lift10 = np.array(lift10)
    aero_shear0=np.zeros(100)
    aero_shear10=np.zeros(100)
    for i in range(len(locations0)):
        aero_shear0[i]=-sp.integrate.trapezoid(aero_lift0[i:], locations0[i:])
        aero_shear10[i]=-sp.integrate.trapezoid(aero_lift10[i:], locations10[i:])

    #Bending moment distribution
    aero_moment_0=np.zeros(100)
    aero_moment_10=np.zeros(100)
    for i in range(100):
        aero_moment_0[i]=-sp.integrate.trapezoid(aero_shear0[i:], locations0[i:])
        aero_moment_10[i]=-sp.integrate.trapezoid(aero_shear10[i:], locations0[i:])
    
    #Calculating the torque distribution
    torque0 = []
    torque10 = []
    for i in range(len(locations0)):
        length = float(locations0[i])+((halfspan-float(locations0[i])/3))
        torque0.append(q*momentcoefficients0[i]*(chords0[i])**2)
        torque10.append(q*momentcoefficients10[i]*(chords10[i])**2)
        

    aero_torque0= np.array(torque0)
    aero_torque10= np.array(torque10)
    T_aero_0 = np.zeros(100)
    T_aero_10 = np.zeros(100)
    for i in range(len(locations0)):
        T_aero_0[i] =  sp.integrate.trapezoid(aero_torque0[i:], locations0[i:])
        T_aero_10[i] =  sp.integrate.trapezoid(aero_torque10[i:], locations10[i:])

    #Induced drag calculations

    aero_induceddrag0 = []
    aero_induceddrag10 = []

    for i in range(len(locations0)):
        aero_induceddrag0.append(q*dragcoefficients0[i]*chords0[i])
        aero_induceddrag10.append(q*dragcoefficients10[i]*chords10[i])
        
    ID_aero_0 = np.zeros(100)
    ID_aero_10 = np.zeros(100)
    for i in range(len(locations0)):
        ID_aero_0[i] =  sp.integrate.trapezoid(aero_induceddrag0[i:], locations0[i:])
        ID_aero_10[i] =  sp.integrate.trapezoid(aero_induceddrag10[i:], locations10[i:])
    
    #Calculate the distributed desired lift coefficient and the corresponding AoA

    def desired_CL(CLd):

        CLd_distributed = []
        CMd_distributed = []
        Cidd_distributed = []
        alpha_d = 0

        for i in range(100):
            CLd_y= float(liftcoefficients0[i]) + ((CLd-CL0)/(CL10-CL0))*(float(liftcoefficients10[i])-float(liftcoefficients0[i]))
            CMd_y= float(momentcoefficients0[i]) + ((CLd-CL0)/(CL10-CL0))*(float(momentcoefficients10[i])-float(momentcoefficients0[i]))
            Cidd_y= float(dragcoefficients0[i]) + ((CLd-CL0)/(CL10-CL0))*(float(dragcoefficients10[i])-float(dragcoefficients0[i]))
            CLd_distributed.append(CLd_y)
            CMd_distributed.append(CMd_y)
            Cidd_distributed.append(Cidd_y)

        alpha_d = ((CLd-CL0)/(CL10-CL0))*np.sin(10*np.pi/180)

        return CLd_distributed, alpha_d, CMd_distributed, Cidd_distributed

    CLd_distributed_1, alpha_d_1, CMd_distributed_1, Cidd_distributed_1 = desired_CL(Cld1)
    CLd_distributed_25, alpha_d_25, CMd_distributed_25, Cidd_distributed_25 = desired_CL(Cld2)
    CLd_distributed_min, alpha_d_min, CMd_distributed_min, Cidd_distributed_min = desired_CL(Cld3)
    
    #Calculating the lift distribution for the desired lift coefficient
    def calculate_lift(CLd_distributed, alpha_d, CMd_distributed, Cidd_distributed):

        lift_CLd = []
        torque_CLd = []
        drag_CLd = []
        totlift_CLd = 0
        for i in range(len(locations0)):
            lift_CLd.append(q*CLd_distributed[i]*chords0[i])
            torque_CLd.append(q*CMd_distributed[i]*(chords0[i])**2)
            drag_CLd.append(q*Cidd_distributed[i]*chords0[i])
            totlift_CLd += dy0[i]*lift_CLd[i]

        aero_shear_CLd=np.zeros(100)
        aero_moment_CLd=np.zeros(100)
        aero_torque_CLd=np.zeros(100)
        aero_drag_CLd=np.zeros(100)
        for i in range(len(locations0)):
            aero_shear_CLd[i]=-sp.integrate.trapezoid(lift_CLd[i:], locations0[i:])
            aero_torque_CLd[i] =  sp.integrate.trapezoid(torque_CLd[i:], locations0[i:])
            aero_drag_CLd[i] = sp.integrate.trapezoid(drag_CLd[i:], locations0[i:])

        for i in range(len(locations0)):
            aero_moment_CLd[i]=-sp.integrate.trapezoid(aero_shear_CLd[i:], locations0[i:])

        return aero_torque_CLd, aero_moment_CLd, aero_shear_CLd, aero_drag_CLd

    aero_torque_CLd_1, aero_moment_CLd_1, aero_shear_CLd_1, aero_drag_CLd_1= calculate_lift(CLd_distributed_1, alpha_d_1, CMd_distributed_1, Cidd_distributed_1)
    aero_torque_CLd_25, aero_moment_CLd_25, aero_shear_CLd_25, aero_drag_CLd_25 = calculate_lift(CLd_distributed_25, alpha_d_25, CMd_distributed_25, Cidd_distributed_25)
    aero_torque_CLd_min, aero_moment_CLd_min, aero_shear_CLd_min, aero_drag_CLd_min = calculate_lift(CLd_distributed_min, alpha_d_min, CMd_distributed_min, Cidd_distributed_min)
    
    #plt.plot(locations0, aero_shear_CLd)
    #plt.show()
    
    return aero_shear0, aero_shear10, aero_moment_0, aero_moment_10, ID_aero_0, ID_aero_10, T_aero_0, T_aero_0, CLd_distributed_1, alpha_d_1, aero_torque_CLd_1, aero_moment_CLd_1, aero_shear_CLd_1, aero_drag_CLd_1, CLd_distributed_25, alpha_d_25, aero_torque_CLd_25, aero_moment_CLd_25, aero_shear_CLd_25, aero_drag_CLd_25, CLd_distributed_min, alpha_d_min, aero_torque_CLd_min, aero_moment_CLd_min, aero_shear_CLd_min, aero_drag_CLd_min

aero_shear0, aero_shear10, aero_moment_0, aero_moment_10, ID_aero_0, ID_aero_10, T_aero_0, T_aero_10, CLd_distributed_1, alpha_d_1, aero_torque_CLd_1, aero_moment_CLd_1, aero_shear_CLd_1, aero_drag_CLd_1, CLd_distributed_25, alpha_d_25, aero_torque_CLd_25, aero_moment_CLd_25, aero_shear_CLd_25, aero_drag_CLd_25, CLd_distributed_min, alpha_d_min, aero_torque_CLd_min, aero_moment_CLd_min, aero_shear_CLd_min, aero_drag_CLd_min = calculate_aeroloads(lines10, rho, v, q)
