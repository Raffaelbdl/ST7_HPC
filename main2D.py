import matplotlib.pyplot as plt
import numpy as np

from utils import plots

### CONFIG ###
norm = "Inf" # "Inf", "L2"
highest_only = True

with_relief = True
with_stations = True
with_source = True
with_signals = True

### PATH ###
path_to_stations = "./2D_coupe/stations_2D_coupe"
# simulation_name1 = "2D_pas_20m_meteo0"
# simulation_name2 = "2D_pas_20m_meteo1"
# simulation_name3 = "2D_pas_20m_meteo2"
simulation_name1 = "2D_pas_10m_meteo0"
simulation_name2 = "2D_pas_10m_meteo1"
simulation_name3 = "2D_pas_10m_meteo2"

### GET RELIEF ###
if with_relief:
    x_relief, y_relief = plots._relief()
    relief_kwargs = {
        'c': 'k',
        'alpha': 0.3,
    }

### GET SOURCE ###
if with_source:
    x_source = 19382
    y_source = 4290
    source_kwargs = {
        'c': 'r',
        's': 100,
    }

### GET STATIONS POS ###
if with_stations:
    stationsxy = np.loadtxt(path_to_stations)
    x_stations = stationsxy[..., 1]
    y_stations = stationsxy[..., 2]
    stations_kwargs = {
        'c': 'g',
        's': 20,
    }

### GET STATIONS SIGNALS NORMS ###
if with_signals:
    if norm == "Inf":
        x11, signals_inf1 = plots._scatter_stations_intensity(
            simulation=simulation_name1,
            path_to_stations=path_to_stations,
            norm="Inf"
        )
        x12, signals_inf2 = plots._scatter_stations_intensity(
            simulation=simulation_name2,
            path_to_stations=path_to_stations,
            norm="Inf"
        )
        x13, signals_inf3 = plots._scatter_stations_intensity(
            simulation=simulation_name3,
            path_to_stations=path_to_stations,
            norm="Inf"
        )
    elif norm == "L2":
        x21, signals_l21 = plots._scatter_stations_intensity(
            simulation=simulation_name1,
            path_to_stations=path_to_stations,
            norm="L2"
        )
        x22, signals_l22 = plots._scatter_stations_intensity(
            simulation=simulation_name2,
            path_to_stations=path_to_stations,
            norm="L2"
        )
        x23, signals_l23 = plots._scatter_stations_intensity(
        simulation=simulation_name3,
        path_to_stations=path_to_stations,
        norm="L2"
    )
    else:
        raise NotImplementedError(
            "Norm " + norm + " is not implemented")


def main():

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Altitude (m)")


    legend_1 = []
    legend_2 = []

    if with_relief:
        # Plot relief
        ax1.plot(x_relief, y_relief, **relief_kwargs)
        legend_1.append("Relief")

    if with_stations:
        # Plot stations
        ax1.scatter(x_stations, y_stations, **stations_kwargs)
        legend_1.append("Stations")

    if with_source:
        # Plot source
        ax1.scatter(x_source, y_source, **source_kwargs)
        legend_1.append("Source")

    ax1.legend(legend_1, loc='upper left')

    if with_signals:

        if highest_only:
            # Plot highest signals
            if norm == "Inf":
                highest_signals = plots.get_highest_2D(
                    x_stations=x11,
                    signals=[signals_inf1, signals_inf2, signals_inf3]
                )
                for i, h_signal in enumerate(highest_signals):
                    ax2.scatter(
                        h_signal[..., 0],
                        h_signal[..., 1]
                    )
            
            elif norm == "L2":
                highest_signals = plots.get_highest_2D(
                    x_stations=x21,
                    signals=[signals_l21, signals_l22, signals_l23]
                )
                for i, h_signal in enumerate(highest_signals):
                    ax2.scatter(
                        h_signal[..., 0],
                        h_signal[..., 1]
                    )
        
        else:
            # Plot all signals
            if norm == "Inf":
                ax2.scatter(x11, signals_inf1, c='k')
                ax2.scatter(x12, signals_inf2, c='orange')
                ax2.scatter(x13, signals_inf3, c='b')
                legend_2 += [
                    "Norme Infinie Meteo 1", 
                    "Norme Infinie Meteo 2", 
                    "Norme Infinie Meteo 3"
                ]

            elif norm == "L2":
                ax2.scatter(x21, signals_l21, c='k')
                ax2.scatter(x22, signals_l22, c='orange')
                ax2.scatter(x23, signals_l23, c='b')
                legend_2 += [
                    "Norme 2 Meteo 1", 
                    "Norme 2 Meteo 2", 
                    "Norme 2 Meteo 3"
                ]
        
        ax2.legend(legend_2, loc='upper right')
        ax2.set_ylabel("Surpression (Pa)")

    plt.show()


if __name__ == "__main__":

    main()