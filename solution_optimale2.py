import matplotlib.pyplot as plt
import numpy as np

from simulations import plots

### PATH ###
path_to_stations = "./2D_coupe/stations_2D_coupe"
simulation_name1 = "2D_coupe_10m_meteo1"
simulation_name2 = "2D_coupe_10m_meteo2"
simulation_name3 = "2D_coupe_10m_ssvent"
# simulation_name1 = "2D_coupe_meteo1"
# simulation_name2 = "2D_coupe_meteo2"
# simulation_name3 = "2D_coupe_hors_sol"

### GET RELIEF ###
x_relief, y_relief = plots._relief()
relief_color = 'k'
relief_alpha = 0.3

### GET SOURCE ###
x_source = 19382
y_source = 4290
source_color = 'r'
source_size = 100

### GET STATIONS POS ###
stationsxy = np.loadtxt(path_to_stations)
x_stations = stationsxy[..., 1]
y_stations = stationsxy[..., 2]
stations_color = 'g'
stations_size = 20

### GET STATIONS NUM ###
per_pos = []
for i in range(len(x_stations)):
    if i % 5 == 0:
        per_pos.append(x_stations[i])
per_pos = np.array(per_pos)
per_pos_y = np.ones_like(per_pos)

### GET STATIONS SIGNALS NORMS ###
x11, signals_l2 = plots._scatter_stations_intensity(
    simulation=simulation_name1,
    path_to_stations=path_to_stations,
    norm="L2"
)
x12, signals_l22 = plots._scatter_stations_intensity(
    simulation=simulation_name2,
    path_to_stations=path_to_stations,
    norm="L2"
)
x13, signals_l23 = plots._scatter_stations_intensity(
    simulation=simulation_name3,
    path_to_stations=path_to_stations,
    norm="L2"
)

if __name__ == "__main__":

    fig, ax1 = plt.subplots()


    idx = np.argsort(x11)
    signals_l2 = signals_l2[idx]
    x11 = x11[idx]

    idx11 = np.argsort(x12)
    signals_l22 = signals_l22[idx]
    x12 = x12[idx]

    idx3 = np.argsort(x13)
    signals_l23 = signals_l23[idx]
    x13 = x13[idx]

    intensities = signals_l2
    intensities1= signals_l22
    intensities2=signals_l23


    intensities = np.append(intensities[:51],intensities[69:])
    intensities1= np.append(intensities1[:51],intensities1[69:])
    intensities2 = np.append(intensities2[:51],intensities2[69:])

    intensities = (intensities - np.min(intensities))
    intensities = intensities/np.max(intensities)
    intensities1 = (intensities1 - np.min(intensities1))
    intensities1 = intensities1/np.max(intensities1)
    intensities2 = (intensities2 - np.min(intensities2))
    intensities2 = intensities2/np.max(intensities2)


    ax1.plot(intensities, color="r")
    ax1.plot(intensities1, color = "g")
    ax1.plot(intensities2, color = "b")

    ax1.legend(["Norme 2 1", "Norme 2 2", "Norme 2 3"], loc='upper right')


    ax1.set_ylabel("Surpression (Pa)")

    plt.show()