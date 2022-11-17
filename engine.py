
import numpy as np
import math

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
    
    for i in range(1001):
        
        if i != 0:
            
            y_wing = (36.74/2)*(i/1000)
            
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

    torque = np.array(engine_bending)
    bending = np.array(engine_torque)

    return torque, bending

x = engineload_takeoff(thrust_cruise, sweep_angle, x_co_engine, y_co_engine, z_co_engine)
print(x)





