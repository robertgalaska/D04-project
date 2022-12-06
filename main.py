import numpy as np

from aerodynamicLoads import*
from engine import*
from inertial_loads import*

#Stepsize
y_wing0 = []
for i in range(100):
    y_wing = (36.74 / 2) * (i / 100)
    y_wing0.append(y_wing)


def combine_shearloads(aero_lift0, aero_lift10, inertial_shear):

    total_shear0 = np.add(aero_lift0, inertial_shear)
    total_shear10 = np.add(aero_lift10, inertial_shear)

    fig, axs = plt.subplots(2)
    # Shear diagrams
    # first plot: shear AoA = 0
    axs[0].plot(y_wing0, total_shear0)
    axs[0].set_title('Shear at critical negative load factor')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Shear [N]')
    # second plot: shear AoA = 10
    axs[1].plot(y_wing0, total_shear10, 'tab:orange')
    axs[1].set_title('Shear at critical positive load factor')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Shear [N]')
    fig.tight_layout()
    plt.show()

    return total_shear0, total_shear10

def combine_bendingmoment(aero_moment0, aero_moment10, engine_bending, inertial_moment):
    total_bending_0 = np.add(aero_moment0,engine_bending)
    total_bending_0 = np.add(total_bending_0, inertial_moment)
    total_bending_10 = np.add(aero_moment10, engine_bending)
    total_bending_10 = np.add(total_bending_10, inertial_moment)



    fig, axs = plt.subplots(2)
    # Bending moments
    # first plot: bending moment AoA = 0
    axs[0].plot(y_wing0, total_bending_0)
    axs[0].set_title('Bending moment at critical negative load factor')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Moment [kNm]')
    # second plot: bending moment AoA = 10
    axs[1].plot(y_wing0, total_bending_10, 'tab:orange')
    axs[1].set_title('Bending moment at critical positive load factor')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Moment [kNm]')
    fig.tight_layout()
    plt.show()

    return total_bending_0, total_bending_10

def combine_torque(engine_torque, aero_torque0, aero_torque10):
    total_torque0 = np.add(aero_torque0,engine_torque)
    total_torque10 = np.add(aero_torque10, engine_torque)
    print(aero_torque10)
    fig, axs = plt.subplots(2)
    # torque
    # first plot: torque AoA = 0
    axs[0].plot(y_wing0, total_torque0)
    axs[0].set_title('Torque at critical negative load factor')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Torque [kNm]')
    # second plot: torque AoA = 10
    axs[1].plot(y_wing0, total_torque10, 'tab:orange')
    axs[1].set_title('Torque at critical positive load factor')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Torque [kNm]')
    fig.tight_layout()
    plt.show()

    return total_torque0, total_torque10

combine_shearloads(aero_shear_CLd_min, aero_shear_CLd_25, inertial_shear)
combine_bendingmoment(aero_moment_CLd_min, aero_moment_CLd_25, engine_bending, inertial_moment)
combine_torque(engine_torque, aero_torque_CLd_min, aero_torque_CLd_25)

