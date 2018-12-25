# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:43:40 2018

@author: My Surface Pro
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

location1 = "h2-imp-4run-1.txt"
location2 = "h2-imp-4run-2.txt"
location3 = "h2-imp-4run-3.txt"
location4 = "h2-imp-4run-4.txt"

data1 = np.loadtxt(location1)
data2 = np.loadtxt(location2)
data3 = np.loadtxt(location3)
data4 = np.loadtxt(location4)

step1, energy1 = np.hsplit(data1, [1])
energy1, psips1 = np.hsplit(energy1, [1])
step2, energy2 = np.hsplit(data2, [1])
energy2, psips2 = np.hsplit(energy2, [1])
step3, energy3 = np.hsplit(data3, [1])
energy3, psips3 = np.hsplit(energy3, [1])
step4, energy4 = np.hsplit(data4, [1])
energy4, psips4 = np.hsplit(energy4, [1])

step1_int = step1.astype(int)
n_steps = np.asscalar(step1_int[-1])

energy_average = np.zeros((1, n_steps))

for i in range(n_steps):
    x = (energy1[i - 1] + energy2[i - 1] + energy3[i - 1] + energy4[i - 1])/4
    energy_average[0, i] = x
    
plt.figure()
graph = plt.scatter(step1, energy_average)
plt.show()

