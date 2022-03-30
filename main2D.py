import matplotlib.pyplot as plt
import numpy as np

from simulations import plots

### PATH ###
path_to_stations = "./2D_coupe/stations_2D_coupe"
# simulation_name1 = "2D_pas_20m_meteo0"
# simulation_name2 = "2D_pas_20m_meteo1"
# simulation_name3 = "2D_pas_20m_meteo2"
simulation_name1 = "2D_pas_10m_meteo0"
simulation_name2 = "2D_pas_10m_meteo1"
simulation_name3 = "2D_pas_10m_meteo2"

### GET RELIEF ###
x_relief, y_relief = plots._relief()
relief_kwargs = {
    'c': 'k',
    'alpha': 0.3,
}

### GET SOURCE ###
x_source = 19382
y_source = 4290
source_kwargs = {
    'c': 'r',
    's': 100,
}

### GET STATIONS POS ###
stationsxy = np.loadtxt(path_to_stations)
x_stations = stationsxy[..., 1]
y_stations = stationsxy[..., 2]
stations_kwargs = {
    'c': 'g',
    's': 20,
}

### GET STATIONS SIGNALS NORMS ###
x11, signals_inf1 = plots._scatter_stations_intensity(
    simulation=simulation_name1,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x21, signals_l21 = plots._scatter_stations_intensity(
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
x13, signals_inf3 = plots._scatter_stations_intensity(
    simulation=simulation_name3,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x23, signals_l23 = plots._scatter_stations_intensity(
    simulation=simulation_name3,
    path_to_stations=path_to_stations,
    norm="L2"
)

if __name__ == "__main__":

    norm = "Inf"

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    legend_1 = []
    legend_2 = []

    # Plot relief
    ax1.plot(x_relief, y_relief, **relief_kwargs)
    legend_1.append("Relief")

    # Plot stations
    ax1.scatter(x_stations, y_stations, **stations_kwargs)
    legend_1.append("Stations")

    # Plot source
    ax1.scatter(x_source, y_source, **source_kwargs)
    legend_1.append("Source")

    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Altitude (m)")
    ax1.legend(legend_1, loc='upper left')

    if norm == "Inf":
        ax2.scatter(x11, signals_inf1, c='k')
        ax2.scatter(x12, signals_inf2, c='orange')
        ax2.scatter(x13, signals_inf3, c='b')
        legend_2 += [
            "Norme Infinie Meteo 0", 
            "Norme Infinie Meteo 1", 
            "Norme Infinie Meteo 2"
        ]
    elif norm == "L2":
        ax2.scatter(x21, signals_l21, c='k')
        ax2.scatter(x22, signals_l22, c='orange')
        ax2.scatter(x23, signals_l23, c='b')
        legend_2 += [
            "Norme 2 Meteo 0", 
            "Norme 2 Meteo 1", 
            "Norme 2 Meteo 2"
        ]
    else:
        raise NotImplementedError(
            "Norm " + norm + " is not implemented")
        
    ax2.legend(legend_2, loc='upper right')
    ax2.set_ylabel("Surpression (Pa)")

    plt.show()