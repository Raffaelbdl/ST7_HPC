import os
from typing import List, Tuple, TYPE_CHECKING

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from matplotlib.axes import Axes

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


def plot_relief3D(
    figandax: tuple = None, 
    **kargs
) -> Tuple['Figure', 'Axes']:
    fig, ax = (
        plt.subplots(subplot_kw={"projection": "3d"})
        if figandax is None
        else figandax
    )
    
    x, y, z = _relief3D()
    idx = np.arange(0, len(x), step=100)

    x = x[idx]
    y = y[idx]
    z = z[idx]

    relief_plot = ax.plot_trisurf(x, y, z, **kargs)

    return fig, ax, relief_plot

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


def _scatter_stations_intensity_3D(
    simulation: str,
    path_to_stations: str,
    norm: str
):
    """
    Implemented norms are:
        L2 : sqrt( mean ( square ( surpression ) ) )
        Inf : max ( abs ( surpression ) )
    """
    path_to_te = "./3D_coupe/" + simulation + "/TE/"
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
    ys = stations[..., 2][np.array(ids)]
    signals = np.array(signals)

    return xs, ys, signals 


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
    

def get_highest_3D(
    x_stations: np.ndarray,
    y_stations: np.ndarray,
    signals: List[np.ndarray],
) -> List[np.ndarray]:

    highest_signals = [[] for _ in range(len(signals))]
    n_stations = len(x_stations)

    for i in range(n_stations):
        indice = np.argmax(
            [
                signal[i] for signal in signals
            ]
        )
        highest_signals[indice].append(
            [
                x_stations[i],
                y_stations[i],
                signals[indice][i],
            ]
        )
    
    for i in range(len(highest_signals)):
        highest_signals[i] = np.array(highest_signals[i])
    return highest_signals


def get_highest_2D(
    x_stations: np.ndarray,
    signals: List[np.ndarray],
) -> List[np.ndarray]:

    highest_signals = [[] for _ in range(len(signals))]
    n_stations = len(x_stations)

    for i in range(n_stations):
        indice = np.argmax(
            [
                signal[i] for signal in signals
            ]
        )
        highest_signals[indice].append(
            [
                x_stations[i],
                signals[indice][i],
            ]
        )
    
    for i in range(len(highest_signals)):
        highest_signals[i] = np.array(highest_signals[i])
    return highest_signals
