# Calculating the wing skin
import numpy as np

f = open("naca6409coords.txt", "r")
lines = f.readlines()

x_coordinatewing = []
y_coordinatewing = []

for line in lines:
    coordinate = line.split("  ")
    x_coordinatewing.append(float(coordinate[0]))
    y_coordinatewing.append(float(coordinate[-1]))

x_ofwing = np.array(x_coordinatewing)
y_ofwing = np.array(y_coordinatewing)
points = len(x_ofwing)

distsumx = 0
dist2sumx = 0
distsumy = 0
distsum2y = 0

for i in range(points):
    distx = x_ofwing * ( x_ofwing[i] ** 2 + y_ofwing[i]** 2) ** 0.5
    distsumx += distx
    dist2x = ( x_ofwing[i] ** 2 + y_ofwing[i]** 2) ** 0.5
    dist2sumx += dist2x

    disty = y_ofwing * (x_ofwing[i] ** 2 + y_ofwing[i] ** 2) ** 0.5
    distsumy += distxy
    dist2y = (x_ofwing[i] ** 2 + y_ofwing[i] ** 2) ** 0.5
    dist2sumy += dist2y


xcentroid = distsumx/distsum2x

ycentroid = distsumy/distsum2y


print(xcentroid, ycentroid)



