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

for i in range(points):
    dist = x_ofwing * ( x_ofwing[i] ** 2 + y_ofwing[i]** 2) ** 0.5
    distsum += dist
    dist2 = ( x_ofwing[i] ** 2 + y_ofwing[i]** 2) ** 0.5
    dist2sum += dist2

xcentroid = distsum/distsum2

print(xcentroid)



