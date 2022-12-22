import numpy as np
from centroid import option
from Column_Buckling import tension, compression
from compressivestrength import stressrearspar, stressfrontspar, stressstringer
import matplotlib.pyplot as plt
from aerodynamicLoads import locations0
import math

yieldstress = np.array([276000000]*100)
print(stressstringer, stressfrontspar, stressrearspar)

def tensiongraph(tension, stressrearspar, stressfrontspar, stressstringer):

    K1c = 29*10**6
    Y = 1.1
    stress = 276*10**6

    marginlist = []
    for i in range(len(tension)):
        marginlist.append(max(tension[i], stressstringer[i]))
    marginlist = np.array(marginlist)
    crackstress = marginlist * 2  # safety factor of 2

    marginofsafety = []
    for i in range(len(tension)):
        marginofsafety.append(min(2, yieldstress[i]/tension[i]))
    marginofsafety = np.array(marginofsafety)

    crack = ((K1c / (Y * crackstress)) ** 2) / np.pi
    critical_crack = np.array([0.034]*100)
    print(critical_crack)

    fig, ax = plt.subplots(1,2, constrained_layout = True)
    # make a plot
    # set x-axis label
    ax[0].set_xlabel("Location along halfspan[m]")
    # set y-axis label
    ax[0].set_ylabel("Stress [Pa]")

    ax[0].plot(locations0, yieldstress, '--', label = "Yield stress", color="orange")
    ax[0].plot(locations0, tension, label = "Cross-sectional tension", color="g")
    ax[0].plot(locations0, stressstringer, label="Stringer tension", color="r")
    #ax[0].plot(locations0, stressfrontspar, label = "Front spar tension", color="c")
    #ax[0].plot(locations0, stressrearspar, label = "Rear spar tension", color="mediumorchid")
    ax[0].plot(locations0, crackstress, '--', label="Margin stress", color="black")
    ax[0].legend(loc="upper left")
    ax[0].grid(True)

    """  
    # set x-axis label
    ax[1].set_xlabel("Location along halfspan[m]")
    # set y-axis label
    ax[1].set_ylabel("Crack length [m]")
    ax[1].plot(locations0, crack, label="Crack length", color="black")
    ax[1].plot(locations0, critical_crack, label="Critical crack length", color="orange")
    ax[1].legend(loc="lower left")
    ax[1].grid(True)
    """
    # set x-axis label
    ax[1].set_xlabel("Location along halfspan[m]")
    # set y-axis label
    ax[1].set_ylabel("Margin of safety [-]")
    ax[1].plot(locations0, marginofsafety, color="black")
    ax[1].grid(True)
    plt.show()

    figs, axs = plt.subplots(1,3, constrained_layout = True)
    print(option)
    index = int(option)-1
    # make a plot
    # set x-axis label
    axs[index].set_xlabel("Location along halfspan[m]")
    # set y-axis label
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

def compressiongraph(compression, stressrearspar, stressfrontspar, stressstringer):

    plt.xlabel("Location along halfspan[m]")
    plt.ylabel("Stress [Pa]")
    plt.plot(locations0, compression, label = "Cross-sectional compression", color="g")
    plt.plot(locations0, stressstringer*-1, label="Stringer compression", color="r")
    plt.plot(locations0, stressfrontspar*-1, label = "Front spar compression", color="c")
    plt.plot(locations0, stressrearspar*-1, label = "Rear spar compression", color="mediumorchid")
    plt.legend(loc="lower left")
    plt.grid(True)
    plt.show()

    return

#compressiongraph(compression, stressrearspar, stressfrontspar, stressstringer)
tensiongraph(tension, stressrearspar, stressfrontspar, stressstringer)