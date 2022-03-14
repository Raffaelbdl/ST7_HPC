import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

path_to_te = "./2D_coupe/2D_coupe_1/TE/"
# num_stations = 7040
num_stations = 98
stations = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]
num_stations = len(stations)

array = np.loadtxt(open(os.path.join(path_to_te, "STATION_ST50")))

y = array[..., 1] 
x = array[..., 0]


plt.plot(x, y)
plt.ylabel("Surpression (Pa)")
plt.xlabel("Temps (s)")

plt.show()
