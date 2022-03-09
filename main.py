import matplotlib.pyplot as plt
import numpy as np

from simulations import plots

### PATH ###
path_to_stations = "./2D_coupe/stations_2D_coupe"
simulation_name = "2D_coupe_1"

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

### GET STATIONS SIGNALS NORMS ###
x1, signals_inf = plots._scatter_stations_intensity(
    simulation=simulation_name,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x2, signals_l2 = plots._scatter_stations_intensity(
    simulation=simulation_name,
    path_to_stations=path_to_stations,
    norm="L2"
)

if __name__ == "__main__":

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot(
        x_relief, y_relief, 
        c=relief_color, alpha=relief_alpha,
    )
    ax1.scatter(
        x_stations, y_stations, 
        c=stations_color, s=stations_size,   
    )
    ax1.scatter(
        x_source, y_source, 
        c=source_color, s=source_size,
    )
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Altitude (m)")
    ax1.legend(["Relief", "Stations", "Source"], loc='upper left')

    norm = "L2"
    if norm == "Inf":
        ax2.scatter(x1, signals_inf)
        ax2.legend(["Norme Infinie"], loc='upper right')
    elif norm == "L2":
        ax2.scatter(x2, signals_l2)
        ax2.legend(["Norme 2"], loc='upper right')
    ax2.set_ylabel("Surpression (Pa)")

    plt.show()