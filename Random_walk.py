import random
import numpy as np
import matplotlib.pyplot as plt


def random_walk(n, a):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['Up', 'Down', 'Left', 'Right'])
        if step == 'Up':
            y = y + a
        elif step == 'Down':
            y = y - a
        elif step == 'Right':
            x = x + a
        else:
            x = x - a
    return (x, y)


number_of_walks = 3000
length = 401
step_length = 1

walk_size_array = np.zeros((1, length))
average_distance_array = np.zeros((1, length))
sqrt_walk_size_array = np.zeros((1, length))

for walk_length in range(1, length):
    sum_distance = 0

    for i in range(number_of_walks):
       (x, y) = random_walk(walk_length, step_length) 
       distance = np.sqrt(abs(x)*abs(x) + abs(y)*abs(y))
       sum_distance += distance
    average_distance = float(sum_distance) / number_of_walks
    walk_size_array[0, walk_length] = walk_length
    average_distance_array[0, walk_length] = float(average_distance)
    sqrt_walk_size_array[0, walk_length] = np.sqrt(walk_length)
   
    print("walk size = ", walk_length, " average distance = ", average_distance)

plt.figure()
walk = plt.scatter(walk_size_array, average_distance_array)
sqrt_walk = plt.scatter(walk_size_array, sqrt_walk_size_array)
plt.xlabel("Walk size")
plt.ylabel("Average distance")
plt.show()
