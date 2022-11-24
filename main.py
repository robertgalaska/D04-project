from aerodynamicLoads import*
from engine import*
from inertial_loads import*

def combine_shearloads(aero_lift0, aero_lift10):
    total_shear_0 = np.add(aero_lift0)
    total_shear_10 = aero_lift10

def combine_bendingmoment(aero_moment0, aero_moment10, engine_bending, inertial_moment):
    total_bending_0 = np.add(aero_moment0,engine_bending)
    total_bending_0 = np.add(total_bending_0, inertial_moment)
    total_bending_10 = np.add(aero_moment10, engine_bending)
    total_bending_10 = np.add(total_bending_10, inertial_moment)

    #Stepsize
    y_wing0 = []
    for i in range(100):
        y_wing = (36.74 / 2) * (i / 100)
        y_wing0.append(y_wing)

    fig, axs = plt.subplots(2)
    # first plot: torque
    axs[0].plot(y_wing0, total_bending_0)
    axs[0].set_title('Moment at angle of attack at 0 deg [Nm]')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Moment [kNm]')
    # second plot: bending moment
    axs[1].plot(y_wing0, total_bending_10, 'tab:orange')
    axs[1].set_title('Moment at angle of attack at 10 deg [Nm]')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Moment [Nm]')
    fig.tight_layout()
    plt.show()

combine_bendingmoment(aero_moment0, aero_moment10, engine_bending, inertial_moment)





