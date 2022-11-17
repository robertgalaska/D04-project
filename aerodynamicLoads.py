import numpy as np
import scipy as sp
from scipy import interpolate

f = open("MainWing_a=0.00_v=10.00ms.txt", "r")
lines = f.readlines()
f.close()
"""
listedvalues= np.zeros((1,13))
array1= np.array[]
#print(listedvalues)
#for line in lines[40:59]:
 #   values = line.split("   ")
    #listedvalues.append[values]
    #print(listedvalues)
    #print(values)
for line in lines[40:59]:
    row=np.array(line)
    array1.append(row)
print(array1)
"""
zerolist = np.array((0,0,0,0,0,0,0,0,0,0,0,0,0))
i = 0
for line in lines[40:59]:

    values = line.split("   ")

    valuelist = np.array(values)

    if i == 0:
        array_values = np.vstack((zerolist, valuelist))
    else:
        array_values = np.vstack((array_values, valuelist))
    i+=1

print(array_values)

locations=[]
liftcoefficients=[]
chords=[]
for i in range(20):
    locations.append(array_values[i,1])
    liftcoefficients.append(array_values[i,4])
    chords.append(array_values[i,2])
print(locations, liftcoefficients, chords)





"""
a0 = np.genfromtxt('MainWing_a=0.00_v=10.00ms.txt', skip_header= 20, skip_footer= 11)

a0 = open('MainWing_a=0.00_v=10.00ms.txt', 'r')
a0res = a0.read()
print(a0res)

a10 = open('MainWing_a=10.00_v=10.00ms.txt', 'r')
a10res = a10.read()
print(a10res)


x = [0,1,2.5,3.8,5.5,7.5,10,14,20]
y = [1.5,1.4,1.2,1.1,1.4,1.6,1.8,2.2,3.2]
f = sp.interpolate.interp1d(x,y,kind='linear',fill_value="extrapolate")
g = sp.interpolate.interp1d(x,y,kind='cubic',fill_value="extrapolate")
print(f(2.5), g(2.5)) ## 1.2 as expected
print(f(6.5), g(6.5)) ## 1.5 for f, 1.529 for g
print(f(22), g(22)) ## 3.533 for f, 3.713 for g
'MainWing_a=0.00_v=10.00ms.txt'
"""