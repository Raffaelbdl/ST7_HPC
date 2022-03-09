from pyexpat.errors import XML_ERROR_RECURSIVE_ENTITY_REF
import matplotlib.pyplot as plt
import numpy as np

from simulations import plots

### PATH ###
path_to_stations = "./2D_coupe/stations_2D_coupe"
simulation_name1 = "2D_coupe_meteo1"
simulation_name2 = "2D_coupe_hors_sol"

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
x1, signals_inf = plots._scatter_stations_intensity(
    simulation=simulation_name1,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x2, signals_l2 = plots._scatter_stations_intensity(
    simulation=simulation_name1,
    path_to_stations=path_to_stations,
    norm="L2"
)
x12, signals_inf2 = plots._scatter_stations_intensity(
    simulation=simulation_name2,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x22, signals_l22 = plots._scatter_stations_intensity(
    simulation=simulation_name2,
    path_to_stations=path_to_stations,
    norm="L2"
)

if __name__ == "__main__":

    # fig, ax1 = plt.subplots()
    # ax2 = ax1.twinx()

    # ax1.plot(
    #     x_relief, y_relief, 
    #     c=relief_color, alpha=relief_alpha,
    # )
    # ax1.scatter(
    #     x_stations, y_stations, 
    #     c=stations_color, s=stations_size,   
    # )
    # ax1.scatter(
    #     x_source, y_source, 
    #     c=source_color, s=source_size,
    # )
    # ax1.set_xlabel("X (m)")
    # ax1.set_ylabel("Altitude (m)")
    # ax1.legend(["Relief", "Stations", "Source"], loc='upper left')

    # norm = "L2"
    # if norm == "Inf":
    #     ax2.scatter(x1, signals_inf, c='cyan')
    #     ax2.scatter(x12, signals_inf2, c='pink')
    #     ax2.legend(["Norme Infinie 1", "Norme Infinie 2"], loc='upper right')
    # elif norm == "L2":
    #     ax2.scatter(x2, signals_l2, c='cyan')
    #     ax2.scatter(x22, signals_l22, c='pink')
    #     ax2.legend(["Norme 2 1", "Norme 2 2"], loc='upper right')
    # ax2.set_ylabel("Surpression (Pa)")

    # ax2.scatter(per_pos, per_pos_y, marker="x")
    
    plots.plot_station_signal("2D_coupe_hors_sol", 36, c='r')
    plots.plot_station_signal("2D_coupe_meteo1", 36, c='g')


    plt.show()