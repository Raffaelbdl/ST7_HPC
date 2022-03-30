"""Functions for creating and displaying data
"""

import os
from typing import List, Tuple, TYPE_CHECKING

import numpy as np
import matplotlib.pyplot as plt

if TYPE_CHECKING:
    from matplotlib.figure import Figure
    from matplotlib.axes import Axes
    from matplotlib.collections import PathCollection


def _relief(
    relief_path: str = "./2D_coupe/topoIS_2D_ymax.dat"
) -> Tuple[np.ndarray]:
    """Loads 2D relief
    
    Returns:
        x (np.ndarray), y (np.ndarray)
    """
    with open(relief_path, "r") as f:
        topology = np.loadtxt(f)
    
    x = topology[..., 0]
    y = topology[..., 2]

    return x, y


def _relief3D(
    relief_path: str = "./3D_coupe/topoIS_3D.dat"
) -> Tuple[np.ndarray]:
    """Loads 3D relief
    
    Returns:
        x (np.ndarray), y (np.ndarray), z (np.ndarray)
    """
    with open(relief_path, "r") as f:
        topology = np.loadtxt(f)

    x = topology[..., 0]
    y = topology[..., 1]
    z = topology[..., 2]

    return x, y, z


def plot_relief(
    relief_path: str = "./2D_coupe/topoIS_2D_ymax.dat",
    **args
) -> 'PathCollection':
    """Plots 2D relief"""
    x, y = _relief(relief_path)

    relief_plot = plt.plot(x, y, **args)

    return relief_plot


def plot_relief3D(
    figandax: tuple = None, 
    relief_path: str = "./3D_coupe/topoIS_3D.dat",
    **kargs
) -> Tuple['Figure', 'Axes', 'PathCollection']:
    """Plots 3D relief
    
    Returns:
        fig (mpl.Figure), ax (mpl.Axes), relief_plot 
    """
    fig, ax = (
        plt.subplots(subplot_kw={"projection": "3d"})
        if figandax is None
        else figandax
    )
    
    x, y, z = _relief3D(relief_path)
    idx = np.arange(0, len(x), step=100) # divide number of vertices by 100

    x = x[idx]
    y = y[idx]
    z = z[idx]

    relief_plot = ax.plot_trisurf(x, y, z, **kargs)

    return fig, ax, relief_plot


def scatter_source(
    x_source: int = 19392, 
    y_source: int = 4290, 
    **args
) -> 'PathCollection':
    """Plots 2D source"""

    source_plot = plt.scatter(x_source, y_source, **args)

    return source_plot


def scatter_stations(
    path_to_stations: str,
    **args
) -> 'PathCollection':
    """Plots 2D stations"""

    stations = np.loadtxt(path_to_stations)

    station_plot = plt.scatter(stations[..., 0], stations[..., 1], **args)

    return station_plot


def _stations_intensity(
    stations_name: str,
    path_to_te: str,
    norm: str
) -> Tuple[List[int], List[float]]:

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
    
    return ids, signals


def _scatter_stations_intensity(
    simulation: str,
    path_to_stations: str,
    norm: str
) -> Tuple[np.ndarray]:
    """Gets 2D stations norms

    Implemented norms are:
        L2 : sqrt( mean ( square ( surpression ) ) )
        Inf : max ( abs ( surpression ) )

    Returns:
        xs (np.ndarray): x for all stations
        signals (np.ndarray): norm for all stations
    """
    path_to_te = "./2D_coupe/" + simulation + "/TE/"
    stations_name = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]

    stations = np.loadtxt(path_to_stations)

    ids, signals = _stations_intensity(
        stations_name=stations_name,
        path_to_te=path_to_te,
        norm=norm,
    )

    xs = stations[..., 1][np.array(ids)]
    signals = np.array(signals)

    return xs, signals


def scatter_stations_intensity(
    simulation: str,
    path_to_stations: str,
    norm: str,
    **args,
) -> 'PathCollection':
    """Plots 2D stations norms

    Implemented norms are:
        L2 : sqrt( mean ( square ( surpression ) ) )
        Inf : max ( abs ( surpression ) )
    """
    xs, signals = _scatter_stations_intensity(
        simulation,
        path_to_stations,
        norm
    )

    signals_plot = plt.scatter(xs, signals, **args)
    
    return signals_plot


def _scatter_stations_intensity_3D(
    simulation: str,
    path_to_stations: str,
    norm: str
) -> Tuple[np.ndarray]:
    """Gets 3D stations norms

    Implemented norms are:
        L2 : sqrt( mean ( square ( surpression ) ) )
        Inf : max ( abs ( surpression ) )

    Returns:
        xs (np.ndarray): x for all stations
        ys (np.ndarray): y for all stations
        signals (np.ndarray): norm for all stations
    """
    path_to_te = "./3D_coupe/" + simulation + "/TE/"
    stations_name = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]

    stations = np.loadtxt(path_to_stations)

    ids, signals = _stations_intensity(
        stations_name=stations_name,
        path_to_te=path_to_te,
        norm=norm
    )

    xs = stations[..., 1][np.array(ids)]
    ys = stations[..., 2][np.array(ids)]
    signals = np.array(signals)

    return xs, ys, signals 


def plot_station_signal(
    simulation: str, 
    station: int,
    **args,
) -> 'PathCollection':
    """Plots signal for a given station"""
    path_to_te = "./2D_coupe/" + simulation + "/TE/"
    station = "STATION_ST" + str(station)

    try:
        station_array = np.loadtxt(open(os.path.join(path_to_te, station)))
    except:
        print(station + " does not exist in simulation")
        raise IOError

    timeline = station_array[..., 0]
    signal = station_array[..., 1]

    signal_plot = plt.plot(timeline, signal, **args)
    
    return signal_plot


def get_highest_3D(
    x_stations: np.ndarray,
    y_stations: np.ndarray,
    signals: List[np.ndarray],
) -> List[np.ndarray]:
    """Gets highest value between many signals for each station
    
    Useful for coloring scatter 3D plots

    Returns:
        highest_signal (List[np.ndarray]): each element is the array of values to plot for each signal
    """

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
    """Gets highest value between many signals for each station
    
    Useful for coloring scatter 2D plots

    Returns:
        highest_signal (List[np.ndarray]): each element is the array of values to plot for each signal
    """

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
