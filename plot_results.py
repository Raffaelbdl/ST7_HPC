import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

path_to_te = "./2D_coupe/2D_coupe_1/TE/"
# num_stations = 7040
num_stations = 98
stations = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]
num_stations = len(stations)

max_intensity = - np.inf
max_index = 0
max_array = None
# for i in range(num_stations):
#     station = stations[i]
#     with open(os.path.join(path_to_te, station), "r") as f:
#         array = np.loadtxt(f)
#     c = np.max(np.abs(array[..., 1]))
#     if c > max_intensity:
#         max_index = i
#         max_intensity = c
#         max_array = array
array = np.loadtxt(open(os.path.join(path_to_te, "STATION_ST20")))

y = array[..., 1]
x = array[..., 0]

print(f"STATION_ST{max_index} is the best")

plt.plot(x, y)
plt.show()
