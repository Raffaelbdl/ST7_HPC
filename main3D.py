"""Main python file for 3D plots"""

import os

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from utils import plots, generate_stations

### CONFIG ###
norm = "Inf" # "Inf", "L2"
highest_only = True

with_relief = False
with_stations = False
with_source = True
with_signals = True

### PATH ###
path_to_stations = "./3D_coupe/stations_3D_coupe"
simulation_name1 = "3D_pas_100m_meteo0"
simulation_name2 = "3D_pas_100m_meteo1"
simulation_name3 = "3D_pas_100m_meteo2"

if not os.path.isfile(path_to_stations):
    generate_stations.save_stations_3D(
        simulation=simulation_name1,
        save_path=path_to_stations
    )
    

### GET RELIEF ###
if with_relief:
    x_relief, y_relief, z_relief = plots._relief3D()
    relief_kwargs = {
        'antialiased': True,
        'cmap': 'terrain',
    }

### GET SOURCE ###
if with_source:
    x_source = 14412
    y_source = 16624
    z_source = 1900
    source_kwargs = {
        'c': 'r',
        's': 100,
    }

### GET STATIONS POS ###
if with_stations:
    stationsxyz = np.loadtxt(path_to_stations)
    x_stations = stationsxyz[..., 1]
    y_stations = stationsxyz[..., 2]
    z_stations = stationsxyz[..., 3]
    stations_kwargs = {
        'c': 'g',
        's': 20,
    }

### GET STATIONS SIGNALS NORMS ###
if with_signals:
    if norm == "Inf":
        x11, y11, signals_inf1 = plots._scatter_stations_intensity_3D(
            simulation=simulation_name1,
            path_to_stations=path_to_stations,
            norm="Inf"
        )
        x12, y12, signals_inf2 = plots._scatter_stations_intensity_3D(
            simulation=simulation_name2,
            path_to_stations=path_to_stations,
            norm="Inf"
        )
        x13, y13, signals_inf3 = plots._scatter_stations_intensity_3D(
            simulation=simulation_name3,
            path_to_stations=path_to_stations,
            norm="Inf"
        )
    elif norm == "L2":
        x21, y21, signals_l21 = plots._scatter_stations_intensity_3D(
            simulation=simulation_name1,
            path_to_stations=path_to_stations,
            norm="L2"
        )
        x22, y22, signals_l22 = plots._scatter_stations_intensity_3D(
            simulation=simulation_name2,
            path_to_stations=path_to_stations,
            norm="L2"
        )
        x23, y23, signals_l23 = plots._scatter_stations_intensity_3D(
            simulation=simulation_name3,
            path_to_stations=path_to_stations,
            norm="L2"
        )


def main():

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    legend = [[], []]

    if with_relief:
        # Plot relief (does not work with legend)
        fig, ax, _ = plots.plot_relief3D(
            figandax=(fig, ax), 
            **relief_kwargs
        )
        fake_line = mpl.lines.Line2D([0], [0], linestyle=None, c='brown')
        legend[0].append(fake_line)
        legend[1].append("Relief")

    if with_stations:
        # Plot stations
        stations_plot = ax.scatter3D(
            x_stations,
            y_stations,
            z_stations,
            **stations_kwargs,
        )
        legend[0].append(stations_plot)
        legend[1].append("Stations")
        ax.set_zlabel("Altitude (m)")

    if with_source:
        # Plot source
        z_source = 0. # set to 0 for vizualizing signals
        source_plot = ax.scatter3D(
            x_source,
            y_source,
            z_source,
            **source_kwargs,
        )
        legend[0].append(source_plot)
        legend[1].append("Source")
    
    if with_signals:

        if highest_only:
            # Plot highest signals
            if norm == "Inf":
                highest_signals = plots.get_highest_3D(
                    x_stations=x11,
                    y_stations=y11,
                    signals=[signals_inf1, signals_inf2, signals_inf3]
                )
                for i, h_signal in enumerate(highest_signals):
                    signal_plot = ax.scatter3D(
                        h_signal[..., 0],
                        h_signal[..., 1],
                        h_signal[..., 2],
                    )
                    legend[0].append(signal_plot)
                    legend[1].append(f"Norme Infinie Meteo {i}")

            elif norm == "L2":
                highest_signals = plots.get_highest_3D(
                    x_stations=x21,
                    y_stations=y21,
                    signals=[signals_l21, signals_l22, signals_l23]
                )
                for i, h_signal in enumerate(highest_signals):
                    signal_plot = ax.scatter3D(
                        h_signal[..., 0],
                        h_signal[..., 1],
                        h_signal[..., 2],
                    )
                    legend[0].append(signal_plot)
                    legend[1].append(f"Norme 2 Meteo {i}")

            else:
                raise NotImplementedError(
                    "Norm " + norm + " is not implemented")

        else:
            # Plot all signals
            if norm == "Inf":
                signal_plot1 = ax.scatter3D(x11, y11, signals_inf1, c='k', zorder=20)
                signal_plot2 = ax.scatter3D(x12, y12, signals_inf2, c='orange', zorder=1)
                signal_plot3 = ax.scatter3D(x13, y13, signals_inf3, c='b', zorder=0)
                legend[0] += [
                    signal_plot1,
                    signal_plot2,
                    signal_plot3
                ]
                legend[1] += [
                    "Norme Infinie Meteo 1", 
                    "Norme Infinie Meteo 2", 
                    "Norme Infinie Meteo 3",
                ]
            
            elif norm == "L2":
                signal_plot1 = ax.scatter3D(x21, y21, signals_l21, c='k')
                signal_plot2 = ax.scatter3D(x22, y22, signals_l22, c='orange')
                signal_plot3 = ax.scatter3D(x23, y23, signals_l23, c='b')
                legend[0] += [
                    signal_plot1,
                    signal_plot2,
                    signal_plot3
                ]
                legend[1] += [
                    "Norme 2 Meteo 1", 
                    "Norme 2 Meteo 2", 
                    "Norme 2 Meteo 3",
                ]
            
            else:
                raise NotImplementedError(
                    "Norm " + norm + " is not implemented")

        ax.set_zlabel("Surpression (Pa)")

    ax.legend(legend[0], legend[1], loc="upper left")
    plt.show()


if __name__ == "__main__":

    main()