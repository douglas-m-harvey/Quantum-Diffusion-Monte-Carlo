# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:02:22 2018

@author: Douglas
"""

import numpy as np
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d


"""
- import data file 
- split into energy array and separate coordinate arrays for both 
  particles
- create x-y plane radius array for both particles
"""
coordinate_array = np.loadtxt("h-hbar-imp.txt")
(energy, x1, y1, z1, x2, y2, z2) = np.split(coordinate_array, 7, axis = 1)
coordinate_array_shape = np.shape(coordinate_array)
r1 = np.zeros((coordinate_array_shape[0], 1))
r2 = np.zeros((coordinate_array_shape[0], 1))
for i in range(coordinate_array_shape[0]):
    r1[i, 0] = np.sqrt(x1[i, 0]**2 + y1[i, 0]**2)
    r2[i, 0] = np.sqrt(x2[i, 0]**2 + y2[i, 0]**2)

"""
- set cartesian coordinates of the 2 fixed particles
- set upper and lower bounds of the plot
- set the 'resolution' of the probability plot
"""
posx1 = 0
posy1 = 0
posx2 = 0.7408
posy2 = 0
xmin = -1.7
xmax = 2.5
ymin = -0.2
ymax = 4
res = 500


def probability(input_array, resolution):
    
    division_size = float(np.ptp(input_array, axis = 0))/resolution
    sorted_input_array = np.sort(input_array, axis = 0)

    n = np.amin(sorted_input_array)
    bin_array = np.zeros((resolution, 1))
    bin_array_shape = np.shape(bin_array)
    for i in range(bin_array_shape[0]):
        n += division_size
        bin_array[i] = n
        
    count_array = np.zeros((resolution, 1))
    count_array_shape = np.shape(count_array)
    input_array_shape = np.shape(input_array)
    for i in range(count_array_shape[0]):
        m = 0
        for j in range(input_array_shape[0]):
            if (bin_array[i] - division_size/2) < sorted_input_array[j] \
            < (bin_array[i] + division_size/2):
                m += 1
                count_array[i] = m
      
    probability_array = count_array*np.sqrt(resolution)/np.linalg.norm\
    (count_array, axis = 0)
    coefficient_array = poly.polyfit(np.ravel(bin_array), \
                                     np.ravel(probability_array), \
                                     int(round(res/10)))
    probability_plot_array = poly.polyval(sorted_input_array, \
                                          coefficient_array)
        
    return (probability_plot_array, probability_array, bin_array)


pl1, pr1, bi1 = probability(z1, res)
pl2, pr2, bi2 = probability(z2, res)
c = np.sort(pl1, axis = 0)

plt.figure()
plt.scatter(z1, r1, color = '#71D71C')
plt.scatter(z2, r2, color = '#F15B20')
#plt.scatter(bi1, pr1)
#plt.scatter(bi2, pr2)
plt.plot(np.sort(z1, axis = 0), pl1, linewidth = 3, color = '#30AC77')
plt.plot(np.sort(z2, axis = 0), pl2, linewidth = 3, color = '#E03E6F')
plt.scatter(posx1, posy1, marker = "^", color = '#459800')
plt.scatter(posx2, posy2, marker = "^", color = '#AA3000')
plt.text(posx1 - 0.06, posy1 - 0.08, "Fixed Particle 1")
plt.text(posx2 - 0.06, posy2 - 0.08, "Fixed Particle 2")
plt.xlim(np.amin(z1), np.amax(z1))
plt.ylim(ymin, ymax)
plt.show

#fig = plt.figure()
#sub = fig.add_subplot(111, projection = '3d')
#sub.scatter(x1, y1, z1)
#sub.scatter(x2, y2, z2)
#plt.show