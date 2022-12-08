import numpy as np
import math
import matplotlib.pyplot as plt

wing_thickness = 0.05  # in meters
x_co_engine = 0
y_co_engine = 6.34
z_co_engine = 1.2665
thrust_takeoff = 120.64*10**3  # In N
thrust_cruise = 118.68*10**3  # In N

sweep_angle = 34.6 * 2 * math.pi / 360


def engineload_takeoff(thrust_cruise, sweep_angle, x, y, z):
    engine_bending = []
    engine_bendingz = []
    engine_torque = []
    y_wing0 = []

    for i in range(100):

        #if i != 0:

        y_wing = (36.74 / 2) * (i / 100)
        y_wing0.append(y_wing)

        if y_wing <= 6.43:

            x_thrust = thrust_cruise * math.cos(sweep_angle)
            y_thrust = thrust_cruise * math.sin(sweep_angle)
            torque_engine = x_thrust * z
            bending_moment_engine = y_thrust * z
            bending_momentz_engine = -x_thrust * (6.43-y_wing)
            engine_torque.append(torque_engine)
            engine_bending.append(bending_moment_engine)
            engine_bendingz.append(bending_momentz_engine)

        else:
            torque_engine = 0
            bending_moment_engine = 0
            bending_momentz_engine = 0
            engine_torque.append(torque_engine)
            engine_bending.append(bending_moment_engine)
            engine_bendingz.append(bending_momentz_engine)

    torque = np.array(engine_torque)
    bending = np.array(engine_bending)
    y_wing0 = np.array(y_wing0)

    fig, axs = plt.subplots(2)
    # first plot: torque
    axs[0].plot(y_wing0, torque)
    axs[0].set_title('Torque due to the engine thrust [Nm]')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Torque [kNm]')
    # second plot: bending moment
    axs[1].plot(y_wing0, bending, 'tab:orange')
    axs[1].set_title('Moment due to the engine thrust [Nm]')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Moment [kNm]')
    fig.tight_layout()
    plt.show()

    return torque, bending, engine_bendingz

engine_torque, engine_bending, engine_bendingz = engineload_takeoff(thrust_cruise, sweep_angle, x_co_engine, y_co_engine, z_co_engine)
