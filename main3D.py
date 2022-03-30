import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from simulations import plots

### PATH ###
path_to_stations = "./3D_coupe/stations_3D_coupe"
simulation_name1 = "3D_pas_100m_meteo0"
simulation_name2 = "3D_pas_100m_meteo1"
simulation_name3 = "3D_pas_100m_meteo2"

### GET RELIEF ###
x_relief, y_relief, z_relief = plots._relief3D()
relief_kwargs = {
    'antialiased': True,
    'cmap': 'terrain',
}

### GET SOURCE ###
x_source = 14412
y_source = 16624
z_source = 1900
source_kwargs = {
    'c': 'r',
    's': 100,
}

### GET STATIONS POS ###
stationsxyz = np.loadtxt(path_to_stations)
x_stations = stationsxyz[..., 1]
y_stations = stationsxyz[..., 2]
z_stations = stationsxyz[..., 3]
stations_kwargs = {
    'c': 'g',
    's': 20,
}

### GET STATIONS SIGNALS NORMS ###
x11, y11, signals_inf1 = plots._scatter_stations_intensity_3D(
    simulation=simulation_name1,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x21, y21, signals_l21 = plots._scatter_stations_intensity_3D(
    simulation=simulation_name1,
    path_to_stations=path_to_stations,
    norm="L2"
)
x12, y12, signals_inf2 = plots._scatter_stations_intensity_3D(
    simulation=simulation_name2,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x22, y22, signals_l22 = plots._scatter_stations_intensity_3D(
    simulation=simulation_name2,
    path_to_stations=path_to_stations,
    norm="L2"
)
x13, y13, signals_inf3 = plots._scatter_stations_intensity_3D(
    simulation=simulation_name3,
    path_to_stations=path_to_stations,
    norm="Inf"
)
x23, y23, signals_l23 = plots._scatter_stations_intensity_3D(
    simulation=simulation_name3,
    path_to_stations=path_to_stations,
    norm="L2"
)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--norm', 
        required=False, 
        type=str
    )
    parser.add_argument(
        '--highest-only', 
        required=False, 
        action='store_true'
    )

        
    args = parser.parse_args()
    
    norm = args.norm if args.norm else "Inf"
    highest_only = args.highest_only if args.highest_only else False

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    legend = [[], []]

    # Plot relief (does not work with legend)
    fig, ax, relief_plot = plots.plot_relief3D(
        figandax=(fig, ax), 
        **relief_kwargs
    )
    # fake_line = mpl.
    legend[0].append(relief_plot)
    legend[1].append("Relief")

    # # Plot stations
    # ax.scatter3D(
    #     x_stations,
    #     y_stations,
    #     z_stations,
    #     **stations_kwargs,
    # )
    # legend.append("Stations")
    # ax.set_zlabel("Altitude (m)")

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
    
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
        
    # if highest_only:
    #     # Plot highest signals
    #     if norm == "Inf":
    #         highest_signals = plots.get_highest_3D(
    #             x_stations=x11,
    #             y_stations=y11,
    #             signals=[signals_inf1, signals_inf2, signals_inf3]
    #         )
    #         for h_signal in highest_signals:
    #             ax.scatter3D(
    #                 h_signal[..., 0],
    #                 h_signal[..., 1],
    #                 h_signal[..., 2],
    #             )
    #             legend += [
    #                 "Norme Infinie Meteo 1", 
    #                 "Norme Infinie Meteo 2", 
    #                 "Norme Infinie Meteo 3",
    #             ]
    #     elif norm == "L2":
    #         highest_signals = plots.get_highest_3D(
    #             x_stations=x21,
    #             y_stations=y21,
    #             signals=[signals_l21, signals_l22, signals_l23]
    #         )
    #         for h_signal in highest_signals:
    #             ax.scatter3D(
    #                 h_signal[..., 0],
    #                 h_signal[..., 1],
    #                 h_signal[..., 2],
    #             )
    #             legend += [
    #                 "Norme L2 Meteo 1", 
    #                 "Norme L2 Meteo 2", 
    #                 "Norme L2 Meteo 3",
    #             ]
    # else:
    #     # Plot all signals
    #     if norm == "Inf":
    #         ax.scatter3D(x11, y11, signals_inf1, c='k', zorder=20)
    #         ax.scatter3D(x12, y12, signals_inf2, c='orange', zorder=1)
    #         ax.scatter3D(x13, y13, signals_inf3, c='b', zorder=0)
    #         legend += [
    #             "Norme Infinie Meteo 1", 
    #             "Norme Infinie Meteo 2", 
    #             "Norme Infinie Meteo 3",
    #         ]
    #     elif norm == "L2":
    #         ax.scatter3D(x21, y21, signals_l21, c='k')
    #         ax.scatter3D(x22, y22, signals_l22, c='orange')
    #         ax.scatter3D(x23, y23, signals_l23, c='b')
    #         legend += [
    #             "Norme 2 Meteo 1", 
    #             "Norme 2 Meteo 2", 
    #             "Norme 2 Meteo 3",
    #         ]
    #     else:
    #         raise NotImplementedError(
    #             "Norm " + norm + " is not implemented")

    # ax.set_zlabel("Surpression (Pa)")
    ax.legend(legend[0], legend[1])

    plt.show()


