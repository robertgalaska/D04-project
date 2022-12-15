from Column_Buckling import tension, compression
from compressivestrength import stressrearspar, stressfrontspar, stressstringer
import matplotlib.pyplot as plt
from aerodynamicLoads import locations0

yieldstress = [276000000]*100
print(stressstringer, stressfrontspar, stressrearspar)

def tensiongraph(tension, stressrearspar, stressfrontspar, stressstringer):

    plt.plot(locations0, tension, label = "Cross-sectional tension", color="g")
    plt.plot(locations0, stressstringer, label="Stringer tension", color="r")
    plt.plot(locations0, stressfrontspar, label = "Front spar tension", color="c")
    plt.plot(locations0, stressrearspar, label = "Rear spar tension", color="mediumorchid")
    plt.legend(loc="upper left")
    plt.show()

    return

def compressiongraph(compression, stressrearspar, stressfrontspar, stressstringer):

    plt.plot(locations0, compression, label = "Cross-sectional compression", color="g")
    plt.plot(locations0, stressstringer*-1, label="Stringer compression", color="r")
    plt.plot(locations0, stressfrontspar*-1, label = "Front spar compression", color="c")
    plt.plot(locations0, stressrearspar*-1, label = "Rear spar compression", color="mediumorchid")
    plt.legend(loc="upper left")
    plt.show()

    return

compressiongraph(compression, stressrearspar, stressfrontspar, stressstringer)
tensiongraph(tension, stressrearspar, stressfrontspar, stressstringer)