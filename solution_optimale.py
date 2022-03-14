import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

path_to_te1 = "./2D_coupe/2D_coupe_meteo1/TE/"
path_to_te2 = "./2D_coupe/2D_coupe_meteo2/TE/"
path_to_te = "./2D_coupe/2D_coupe_hors_sol/TE/"
stations = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]
stations1 = [s for s in os.listdir(path_to_te1) if "STATION_ST" in s]
stations2 = [s for s in os.listdir(path_to_te2) if "STATION_ST" in s]
num_stations = len(stations)
num_stations1 = len(stations1)
num_stations2 = len(stations2)

## stations_irl = np.loadtxt("stations_2D_coupe_1")

intensities, intensities1, intensities2 = [], [], []
intensities_wout, intensities_wout1, intensities_wout2 = [], [], []

ids, ids1, ids2= [], [], []
for station in stations:
    array = np.loadtxt(open(os.path.join(path_to_te, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensity = np.sqrt(np.mean(np.square(_array[non_nul:])))
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    intensities.append(intensity)
    intensities_wout.append(intensitiy_wout)
   ##i_max.append(intensity_max)

    station_id = int(station[10:])
    ids.append(station_id)

for station in stations1:
    array = np.loadtxt(open(os.path.join(path_to_te1, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensity = np.sqrt(np.mean(np.square(_array[non_nul:])))
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    intensities1.append(intensity)
    intensities_wout1.append(intensitiy_wout)
   ##i_max.append(intensity_max)

    station_id = int(station[10:])
    ids1.append(station_id)

for station in stations2:
    array = np.loadtxt(open(os.path.join(path_to_te2, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensity = np.sqrt(np.mean(np.square(_array[non_nul:])))
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    intensities2.append(intensity)
    intensities_wout2.append(intensitiy_wout)
   ##i_max.append(intensity_max)

    station_id = int(station[10:])
    ids2.append(station_id)

## On place une zone interdite autour de la source
intensities = intensities[:51]+intensities[69:]
intensities1= intensities1[:51]+intensities1[69:]
intensities2 = intensities2[:51]+intensities2[69:]

intensities = (intensities - np.min(intensities))
intensities = intensities/np.max(intensities)
intensities1 = (intensities1 - np.min(intensities1))
intensities1 = intensities1/np.max(intensities1)
intensities2 = (intensities2 - np.min(intensities2))
intensities2 = intensities2/np.max(intensities2)

## Première approche
def f(x):
    return 1/(1+np.exp(15*(0.4-x)))

intensities_sol1 = f(intensities)
intensities1_sol1 = f(intensities1)
intensities2_sol1 = f(intensities2)

plt.plot(intensities1_sol1)
plt.plot(intensities1, color = "r")
plt.show()
sum_sol = intensities1 + intensities2 + intensities
print(np.where(sum_sol == np.max(sum_sol)))
print(sum_sol[50], np.max(sum_sol))