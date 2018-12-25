# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 16:43:40 2018

@author: My Surface Pro
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


data = np.loadtxt("h2-imp2.txt")

data1, data2 = np.hsplit(data, [1])
data2, data3 = np.hsplit(data2, [1])

plt.figure()
graph = plt.scatter(data1, data2)
plt.show()