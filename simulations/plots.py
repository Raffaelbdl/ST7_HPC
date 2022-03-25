import os
from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt

def _relief() -> Tuple[np.ndarray]:
    with open("./2D_coupe/topoIS_2D_ymax.dat", "r") as f:
        topology = np.loadtxt(f)
    
    x = topology[..., 0]
    y = topology[..., 2]

    return x, y


def _relief3D() -> Tuple[np.ndarray]:
    with open("./3D_coupe/topoIS_3D.dat", "r") as f:
        topology = np.loadtxt(f)

    x = topology[..., 0]
    y = topology[..., 1]
    z = topology[..., 2]

    return x, y, z


def plot_relief(**args) -> None:
    x, y = _relief()

    plt.plot(x, y, **args)


def plot_relief3D(**args) -> None:
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    
    x, y, z = _relief3D()
    idx = np.arange(0, len(x), step=100)

    x = x[idx]
    y = y[idx]
    z = z[idx]

    ax.plot_trisurf(x, y, z, **args)

    return fig, ax



def scatter_source(
    x_source: int = 19392, 
    y_source: int = 4290, 
    **args
) -> None:

    x_source = 19392
    y_source = 4290

    plt.scatter(x_source, y_source, **args)


def scatter_stations(
    path_to_stations: str,
    **args
) -> None:

    stations = np.loadtxt(path_to_stations)

    plt.scatter(stations[..., 0], stations[..., 1], **args)


def _scatter_stations_intensity(
    simulation: str,
    path_to_stations: str,
    norm: str
):
    """
    Implemented norms are:
        L2 : sqrt( mean ( square ( surpression ) ) )
        Inf : max ( abs ( surpression ) )
    """
    path_to_te = "./2D_coupe/" + simulation + "/TE/"
    stations_name = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]

    stations = np.loadtxt(path_to_stations)

    ids = []
    signals = []
    for station in stations_name:
        station_array = np.loadtxt(open(os.path.join(path_to_te, station)))

        signal = station_array[..., 1] - 1e5
        try:
            non_zero = np.min(np.where(signal != 0))
        except:
            non_zero = 0
        signal_trunc = signal[non_zero:]

        if norm == "L2":
            signal_trunc = np.sqrt(np.mean(np.square(signal_trunc)))
        elif norm == "Inf":
            signal_trunc = np.max(np.abs(signal_trunc))
        
        signals.append(signal_trunc)
        ids.append(int(station[10:]))

    xs = stations[..., 1][np.array(ids)]
    signals = np.array(signals)

    return xs, signals


def scatter_stations_intensity(
    simulation: str,
    path_to_stations: str,
    norm: str,
    **args,
):
    """
    Implemented norms are:
        L2 : sqrt( mean ( square ( surpression ) ) )
        Inf : max ( abs ( surpression ) )
    """
    
    xs, signals = _scatter_stations_intensity(
        simulation,
        path_to_stations,
        norm
    )

    plt.scatter(xs, signals, **args)
    

def plot_station_signal(
    simulation: str, 
    station: int,
    **args,
):
    path_to_te = "./2D_coupe/" + simulation + "/TE/"
    station = "STATION_ST" + str(station)
    station_array = np.loadtxt(open(os.path.join(path_to_te, station)))

    timeline = station_array[..., 0]
    signal = station_array[..., 1]

    plt.plot(timeline, signal, **args)
    
    

