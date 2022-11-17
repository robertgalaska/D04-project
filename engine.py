import numpy as np
from constants import *

wing_thickness = 0.05      #in meters
x_co_engine = 0
y_co_engine = 6.34
z_co_engine = 1.2665
thrust_takeoff = 120.64     #In kN
thrust_cruise = 118.68      #In kN


sweep_angle = 37.185*2*math.pi/360
print(sweep_angle)

def engineload_takeoff(thrust_cruise, sweep_angle, x,y,z):

    engine_bending = np.ones((1,1)) # multiple with result from def
    print(engine_bending)

    lst_engine_torque = []
    for i in range(75):
        y_wing = i/4
        if y_wing >= 6.43:

            x_thrust = thrust_cruise*math.cos(sweep_angle)
            y_thrust = thrust_cruise*math.sin(sweep_angle)
            torque_engine = x_thrust*z
            bending_moment_engine = y_thrust*z

        else:
            torque_engine = 0
            bending_moment_engine = 0

engineload_takeoff(thrust_cruise, sweep_angle, x_co_engine, y_co_engine, z_co_engine)




