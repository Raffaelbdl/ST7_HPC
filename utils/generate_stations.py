import csv
import numpy as np

def make_stations(
    relief_path: str = "./2D_coupe/topoIS_2D_ymax.dat",
    step: int = 10,
    pas: float = 0.,
) -> np.ndarray:
    """Gets 2D station coordinates"""

    topology = np.loadtxt(relief_path)
    x = topology[..., 0]
    y = topology[..., 2]

    num_stations = len(x) // step
    station_coord = []
    for k in range(num_stations):
        station_coord.append(
            [x[k * step], y[k * step] + 2 * pas]
        )
    
    return np.array(station_coord)


def make_stations_3D(
    relief_path: str = "./3D_coupe/topoIS_3D.dat",
    stepx: int = 15,
    stepy: int = 10,
    pas: float = 0.,
) -> np.ndarray:
    """Gets 3D station coordinates"""

    topology = np.loadtxt(relief_path)
    x = topology[..., 0] # 983 unique
    y = topology[..., 1] # 492 unique
    z = topology[..., 2]

    x_unique = len(np.unique(x))
    y_unique = len(np.unique(y))

    _x_ = np.reshape(x, (y_unique, x_unique))
    _y_ = np.reshape(y, (y_unique, x_unique))
    _z_ = np.reshape(z, (y_unique, x_unique))

    station_coord = []
    for i in range(y_unique//stepy):
        for j in range(x_unique//stepx):
            _x = _x_[i*stepy][j*stepx]
            _y = _y_[i*stepy][j*stepx]
            _z = _z_[i*stepy][j*stepx] + 2 * pas
            station_coord.append([_x, _y, _z])

    return np.array(station_coord)


def save_stations(
    simulation: str,
    save_path: str = "./2D_coupe/stations_2D_coupe",
) -> np.ndarray:
    """Saves 2D stations"""
    sheet = csv.reader(
        open("./2D_coupe/" + simulation + "/TE/STATION_NOM", "r"),
        delimiter = ' '
    )
    for row in sheet:
        if sheet[0][:2] == 'ST':
            num = int(row[0][2:])
            stations.append(
                [
                    num,
                    row[1],
                    row[2]
                ]
            )

    stations = np.array(stations, dtype=np.float32)
    np.savetxt(save_path, stations)

    return stations


def save_stations_3D(
    simulation: str,
    save_path: str = "./3D_coupe/stations_3D_coupe",
) -> np.ndarray:
    """Saves 3D stations"""
    sheet = csv.reader(
        open("./3D_coupe/" + simulation + "/TE/STATION_NOM", "r"),
        delimiter = ' '
    )
    for row in sheet:
        if sheet[0][:2] == 'ST':
            num = int(row[0][2:])
            stations.append(
                [
                    num,
                    row[1],
                    row[2],
                    row[3]
                ]
            )

    stations = np.array(stations, dtype=np.float32)
    np.savetxt(save_path, stations)

    return stations