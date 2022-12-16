import numpy as np

from Column_Buckling import tension, compression
from compressivestrength import stressrearspar, stressfrontspar, stressstringer
import matplotlib.pyplot as plt
from aerodynamicLoads import locations0
import math

yieldstress = [276000000]*100
print(stressstringer, stressfrontspar, stressrearspar)

def tensiongraph(tension, stressrearspar, stressfrontspar, stressstringer):

    K1c = 29*10**6
    Y = 1.1
    stress = 276*10**6

    crackstress = tension*2     #safety factor of 2
    #crack = ((K1c/(Y*crackstress))**2)/np.pi

    marginlist = []
    for i in range(len(tension)):
        marginlist.append(max(tension[i], stressstringer))
    marginlist = np.array(marginlist)

    fig, ax = plt.subplots()
    # make a plot
    # set x-axis label
    ax.set_xlabel("Location along halfspan[m]")
    # set y-axis label
    ax.set_ylabel("Stress [Pa]")

    ax.plot(locations0, yieldstress, '--', label = "Cross-sectional tension", color="orange")
    ax.plot(locations0, tension, label = "Cross-sectional tension", color="g")
    ax.plot(locations0, stressstringer, label="Stringer tension", color="r")
    ax.plot(locations0, stressfrontspar, label = "Front spar tension", color="c")
    ax.plot(locations0, stressrearspar, label = "Rear spar tension", color="mediumorchid")
    ax2 = ax.twinx()
    ax.plot(locations0, crackstress, label="Cracklength", color="black")
    plt.legend(loc="upper left")
    plt.grid(True)
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