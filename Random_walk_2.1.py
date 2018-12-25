# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:21:05 2018

@author: My Surface Pro
"""

import random
import numpy as np
import matplotlib.pyplot as plt

x = 0
y = 0

def random_walk(a, b):
    global x
    global y
    angle = random.uniform(0, 2*np.pi)
    sin = np.sin(angle)
    cos = np.cos(angle)
    x += a*cos
    y += b*sin
    return (x, y)

steps = 10000
step_length_x = 1
step_length_y = 1
value_array_x = np.zeros((1, steps))
value_array_y = np.zeros((1, steps))
x_lim = 150
y_lim = 150

for i in range(0, steps):
    (x, y) = random_walk(step_length_x, step_length_y)
    value_array_x[0, i] = x
    value_array_y[0, i] = y
    
plt.figure()
walk = plt.scatter(value_array_x, value_array_y)
plt.xlim(-x_lim, x_lim)
plt.ylim(-y_lim, y_lim)
plt.show()
