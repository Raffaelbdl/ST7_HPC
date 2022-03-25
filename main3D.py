import matplotlib.pyplot as plt
import numpy as np
from simulations.plots import *

source1 = (19112, 15324, 1900)
source2 = (14412, 16624, 1900)

fig, ax = plot_relief3D(antialiased=True, cmap='terrain')

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

stepx = 15
stepy = 10
station_coord = []
for i in range(492//stepy):
    for j in range(983//stepx):
        _x = _x_[i*stepy][j*stepx]
        _y = _y_[i*stepy][j*stepx]
        _z = _z_[i*stepy][j*stepx]
        station_coord.append([_x, _y, _z])


station_coord = np.array(station_coord)
ax.scatter3D(*source2, c='r', s=100, zorder=10)
print(station_coord.shape)
ax.scatter3D(
    station_coord[..., 0],
    station_coord[..., 1],
    station_coord[..., 2], 
    c='g', 
    s=1
)
plt.show()