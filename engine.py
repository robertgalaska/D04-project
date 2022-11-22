import numpy as np
import math
import matplotlib.pyplot as plt

wing_thickness = 0.05      #in meters
x_co_engine = 0
y_co_engine = 6.34
z_co_engine = 1.2665
thrust_takeoff = 120.64     #In kN
thrust_cruise = 118.68      #In kN


sweep_angle = 37.185*2*math.pi/360

def engineload_takeoff(thrust_cruise, sweep_angle, x,y,z):

    engine_bending = []
    engine_torque = []
    y_wing0 =[]
    
    for i in range(1001):
        
        if i != 0:
            
            y_wing = (36.74/2)*(i/1000)
            y_wing0.append(y_wing)
            
            
            if y_wing >= 6.43:

                
                x_thrust = thrust_cruise*math.cos(sweep_angle)
                y_thrust = thrust_cruise*math.sin(sweep_angle)
                torque_engine = x_thrust*z
                bending_moment_engine = y_thrust*z
                engine_torque.append(torque_engine)
                engine_bending.append(bending_moment_engine)

            else:
                torque_engine = 0
                bending_moment_engine = 0
                engine_torque.append(torque_engine)
                engine_bending.append(bending_moment_engine)

    torque = np.array(engine_torque)
    bending = np.array(engine_bending)
    y_wing0 = np.array(y_wing0)
    print(len(torque))
    print(len(bending))
    print(len(y_wing0))

    #fig, (ax1, ax2) = plt.subplots(2)
    #fig.suptitle('Horizontally stacked subplots')
    #ax1.plot(torque)
    #plt.suptitle('Torque due to the engine [kNm]')
    
    #ax2.plot(bending)
    #plt.title('Moment due to the engine [kNm]')
    #plt.show()


    fig, axs = plt.subplots(2)
    #first plot: torque
    axs[0].plot(y_wing0, torque)
    axs[0].set_title('Torque due to the engine thrust [kNm]')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Torque [kNm]')
    #second plot: bending moment
    axs[1].plot(y_wing0, bending, 'tab:orange')
    axs[1].set_title('Moment due to the engine thrust [kNm]')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Moment [kNm]')
    fig.tight_layout()
    plt.show()

    return torque, bending



x = engineload_takeoff(thrust_cruise, sweep_angle, x_co_engine, y_co_engine, z_co_engine)
print(x)
