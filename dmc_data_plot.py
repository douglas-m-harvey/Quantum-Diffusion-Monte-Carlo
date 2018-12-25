# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:43:40 2018

@author: My Surface Pro
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

group = 1
number = 1
run = 0
location = "h2-imp-" + str(group) + "_" + str(number) + "_" + str(run) + ".txt"

run_number = str(group) + "_" + str(number) + "_" + str(run)
N0 = 10000
dt = 1.21e-20
Nsteps = 45000
Ne0 = 5000
A1 = 0.00
B1 = 0.00

data = np.loadtxt(location)

step, energy = np.hsplit(data, [1])
energy, psips = np.hsplit(energy, [1])

std = np.std(energy[Ne0 - 1: -1])


y_max = -235000
y_min = -550000
plt.figure()
graph = plt.scatter(step, energy)
plt.title('Run number: ' + run_number + ', initial number of walkers = ' + str(N0) + ', final time step = ' + str(dt) + ' seconds, number of steps = ' + str(Nsteps) + ', averaging number = ' + str(Ne0) + ', A1 = ' + str(A1) + ' and B1 = ' + str(B1) + '. Standard deviation is ' + str(std))
plt.xlabel('Step')
plt.ylabel('Energy (cm^-1)')
plt.ylim(y_min, y_max)
plt.show()
