import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

path_to_te = "./2D_coupe/2D_coupe_200s/TE/"
stations = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]
num_stations = len(stations)

stations_irl = np.loadtxt("stations_2D_coupe_1")

intensities = []
intensities_wout = []
i_max = []

ids = []
for station in stations:
    array = np.loadtxt(open(os.path.join(path_to_te, station)))
    _array = array[..., 1] - 1e5
    print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    print(non_nul)

    # valeur efficace
    intensity = np.sqrt(np.mean(np.square(_array[non_nul:])))
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    # norme 1
    intensity_max = np.max(np.abs(_array[non_nul:]))
    

    intensities.append(intensity)
    intensities_wout.append(intensitiy_wout)
    i_max.append(intensity_max)

    station_id = int(station[10:])
    ids.append(station_id)


intensities = np.array(intensities)
intensities_wout = np.array(intensities_wout)
i_max = np.array(i_max)
xs = stations_irl[...,1][np.array(ids)]
ys = stations_irl[..., 2][np.array(ids)]

with open("./2D_coupe/topoIS_2D_ymax.dat", "r") as f:
    topology = np.loadtxt(f)
relief = topology[...,2]
# x = np.arange(len(relief))
x = topology[..., 0]

x_source = 19382
y_source = 4290

fig, ax1 = plt.subplots()

ax1.plot(x, relief, alpha=0.3)
ax1.scatter(xs, ys, c='g')
ax1.scatter(x_source, y_source, c='r', s=100)
ax1.set_ylabel("Altitude  (m)")
ax1.legend(["Source", "Relief", "Stations"], loc='upper left')
ax1.set_xlabel("X (m)")

ax2 = ax1.twinx()
ax2.scatter(xs, intensities, c='pink')
ax2.scatter(xs, i_max, c='cyan')
ax2.set_ylabel("Valeur efficace du signal perçu (Pa^2)")
ax2.legend(["Valeur efficace"], loc='upper right')
# plt.scatter(xs, intensities_wout, c='gray', s=20, marker='x')
# plt.ylim([0, 7000])

# plt.title(path_to_te)
plt.show()
