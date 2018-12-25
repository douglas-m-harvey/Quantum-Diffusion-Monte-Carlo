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

def random_walk(a):
    global x
    global y
    angle = random.uniform(0, 2*np.pi)
    sin = np.sin(angle)
    cos = np.cos(angle)
    x += a*cos
    y += a*sin
    return (x, y)

steps = 100
step_length = 1
value_array_x = np.zeros((1, steps))
value_array_y = np.zeros((1, steps))

for i in range(0, steps):
    (x, y) = random_walk(step_length)
    value_array_x[0, i] = x
    value_array_y[0, i] = y
    
plt.figure()
walk = plt.scatter(value_array_x, value_array_y)
plt.show()
