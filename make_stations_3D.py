import numpy as np
import json
import matplotlib.pyplot as plt

pas = 100
xmin = -10e3
ymin = 1e3
Lx = 40e3
Ly = 11e3

topology = np.loadtxt("./3D_coupe/topoIS_3D.dat")
x = topology[..., 0] # 983 unique
y = topology[..., 1] # 492 unique
z = topology[..., 2]

_x_ = np.reshape(x, (492, 983))
_y_ = np.reshape(y, (492, 983))
_z_ = np.reshape(z, (492, 983))

x_unique = np.unique(x)
y_unique = np.unique(y)

stepx = 1
stepy = 1
station_coord = []
for i in range(492//stepy):
    for j in range(983//stepx):
        _x = x_unique[j]
        _y = y_unique[i]
        _z = _z_[i][j]
        station_coord.append([_x, _y, _z])


station_coords = np.array(station_coord)
print(np.max(station_coords[..., 2]))
print(len(station_coords))
# x_s = station_coords[..., 0]
# y_s = station_coords[..., 1]
# print(len(x_s))
# plt.scatter(x_s, y_s)
# plt.show()
# json.dump(station_coord, open("stations3D.json", "w"))
