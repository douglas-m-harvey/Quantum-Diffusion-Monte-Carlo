# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:02:22 2018

@author: Douglas
"""

import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

coord_row = 100
coord_col = 6
coord_arr = np.zeros((coord_row, coord_col))

for j in range(coord_col):
    for i in range(coord_row):
        coord_arr[i, j] = rn.random()*np.sin(i)
                
(x1, y1, z1, x2, y2, z2) = np.split(coord_arr, 6, axis = 1)

fig = plt.figure()
sub = fig.add_subplot(111, projection = '3d')
sub.scatter(x1, y1, z1)
sub.scatter(x2, y2, z2)
plt.show