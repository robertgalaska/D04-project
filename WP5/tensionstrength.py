import numpy as np
from centroid import option
from Column_Buckling import tension
from compressivestrength import stressrearspar, stressfrontspar, stressstringer
import matplotlib.pyplot as plt
from aerodynamicLoads import locations0

def tensiongraph(tension, stressrearspar, stressfrontspar, stressstringer):

    # constants for formula of crack length
    K1c = 29*10**6
    Y = 1.1
    yieldstress = np.array([276000000] * 100)

    # find the margin stress of 2 times the max stress
    marginlist = []
    for i in range(len(tension)):
        marginlist.append(max(tension[i], stressstringer[i]))
    marginlist = np.array(marginlist)
    crackstress = marginlist * 2  # safety factor of 2

    # critical crack, already calculated in latex
    critical_crack = np.array([0.034]*100)
    print(critical_crack)

    # make plot for only max stresses and crack length
    fig, ax = plt.subplots(1,2, constrained_layout = True)
    ax[0].set_xlabel("Location along halfspan[m]")
    ax[0].set_ylabel("Stress [Pa]")
    ax[0].plot(locations0, yieldstress, '--', label = "Yield stress", color="orange")
    ax[0].plot(locations0, tension, label = "Cross-sectional tension", color="g")
    ax[0].plot(locations0, stressstringer, label="Stringer tension", color="r")
    ax[0].plot(locations0, crackstress, '--', label="Margin stress", color="black")
    ax[0].legend(loc="upper left")
    ax[0].grid(True)
    ax[1].set_xlabel("Location along halfspan[m]")
    ax[1].set_ylabel("Margin of safety [-]")
    ax[1].plot(locations0, marginofsafety, color="black")
    ax[1].grid(True)
    plt.show()

    # make plot for all stresses
    figs, axs = plt.subplots(1,3, constrained_layout = True)
    print(option)
    index = int(option)-1
    axs[index].set_xlabel("Location along halfspan[m]")
    axs[index].set_ylabel("Stress [Pa]")
    #axs[index].plot(locations0, yieldstress, '--', label="Cross-sectional tension", color="orange")
    axs[index].plot(locations0, tension, label="CS-T", color="g")
    axs[index].plot(locations0, stressstringer, label="S-T", color="r")
    axs[index].plot(locations0, stressfrontspar, label = "FS-T", color="c")
    axs[index].plot(locations0, stressrearspar, label = "RS-T", color="mediumorchid")
    #axs[index].plot(locations0, crackstress, '--', label="Margin stress", color="black")
    axs[index].legend(loc="upper left")
    axs[index].grid(True)

    plt.show()

    return

tensiongraph(tension, stressrearspar, stressfrontspar, stressstringer)