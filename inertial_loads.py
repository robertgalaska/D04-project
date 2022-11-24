import matplotlib.pyplot as plt
import numpy as np


def calculate_inertialloads():

    # add your dimensions
    c_r = 6.12
    span = 36.74
    y_wing0 = []

    w_weight = []
    w_shear = []
    w_moment = []

    for i in range(100):

        y_wing = (36.74 / 2) * (i / 100)
        y_wing0.append(y_wing)

        total_weight = 9.65 * y_wing ** 2 - 445.77 * y_wing + 5147.3
        total_shear = -1 * (3.217 * y_wing ** 3 - 222.9 * y_wing ** 2 + 5147.3 * y_wing - 39235.8)
        total_moment = -1 * (0.804 * y_wing ** 4 - 74.3 * y_wing ** 3 + 2573.7 * y_wing ** 2 - 39235.8 * y_wing + 221283.5)

        # engine weight
        if y_wing < 6.43:

            engine_weight = 0
            engine_shear = 34780
            engine_moment = 34780 * y_wing - 224214

            total_weight += engine_weight
            total_shear += engine_shear
            total_moment += engine_moment


        w_weight.append(total_weight)
        w_shear.append(total_shear)
        w_moment.append(total_moment)

    inertial_load = np.array(w_weight)
    inertial_shear = np.array(w_shear)
    inertial_moment = np.array(w_moment)


    fig, axs = plt.subplots(3)
    # first plot: shear
    axs[0].plot(y_wing0, w_weight)
    axs[0].set_title('Weight over the wing[N]')
    axs[0].set_xlabel('Spanwise location [m]')
    axs[0].set_ylabel('Weight [N]')
    # second plot: bending moment

    axs[1].plot(y_wing0, w_shear, 'tab:orange')
    axs[1].set_title('Shear over the wing [N]')
    axs[1].set_xlabel('Spanwise location [m]')
    axs[1].set_ylabel('Shear [N]')
    fig.tight_layout()

    axs[2].plot(y_wing0, w_moment, 'tab:orange')
    axs[2].set_title('Moment over the wing [Nm]')
    axs[2].set_xlabel('Spanwise location [m]')
    axs[2].set_ylabel('Moment [Nm]')
    fig.tight_layout()

    plt.show()

    return inertial_load, inertial_shear, inertial_moment

inertial_load, inertial_shear, inertial_moment = calculate_inertialloads()
