import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

path_to_te = "./2D_coupe/2D_coupe_hors_sol/TE/"
stations = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]
num_stations = len(stations)

stations_irl = np.loadtxt("stations_2D_coupe_1")

intensities = []
intensities_wout = []

ids = []
for station in stations:
    array = np.loadtxt(open(os.path.join(path_to_te, station)))
    _array = array[..., 1] - 1e5
    print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    print(non_nul)
    intensity = np.mean(np.square(_array[non_nul:]))
    intensitiy_wout = np.mean(np.square(array[..., 1] - 1e5))
    intensities.append(intensity)
    intensities_wout.append(intensitiy_wout)

    station_id = int(station[10:])
    ids.append(station_id)


intensities = np.array(intensities)
intensities_wout = np.array(intensities_wout)
xs = stations_irl[...,1][np.array(ids)]
ys = stations_irl[..., 2][np.array(ids)]

with open("./250m/topoIS_2D_ymax.dat", "r") as f:
    topology = np.loadtxt(f)
relief = topology[...,2]
# x = np.arange(len(relief))
x = topology[..., 0]

x_source = 19382
y_source = 4290

plt.scatter(x_source, y_source, c='r', s=100)
plt.plot(x, relief, alpha=0.3)
plt.scatter(xs, intensities)
plt.scatter(xs, intensities_wout, c='gray', s=20, marker='x')
plt.scatter(xs, ys, c='g')
plt.ylim([0, 7000])
plt.show()
