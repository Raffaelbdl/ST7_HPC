import numpy as np
import matplotlib.pyplot as plt


with open("./250m/topoIS_2D_ymax.dat", "r") as f:
    topology = np.loadtxt(f)
relief = topology[...,2]
# x = np.arange(len(relief))
x = topology[..., 0]

x_source = 19382
y_source = 4290

# print(np.where(topology[..., 0] - x_source < 0.0001))

print(x[0], x[-1])
print(len(x))
# xmin = -10e-3
# Lx = 40e3

station_coord = []
stations = []
# 983 -> 49100m
# 5 -> 250m
# 10 -> 500m
for k in range(0, 98):
    coord = (x[k*10], relief[k*10])
    stations.append([k, coord[0], coord[1]])
    station_coord.append(coord)


print(stations)
stations = np.array(stations)
np.savetxt("stations_2D_coupe_1", stations)


print(len(station_coord))
# print(np.array(station_coord))

# plt.scatter(np.array(station_coord)[..., 0], np.array(station_coord)[..., 1], c='g')
plt.scatter(x_source, y_source, c='r', s=100)
plt.plot(x, relief, c='k')
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.show()

# # TODO regarder la transformation du relief dans le script python

# xmin = -10e3
# ymin = 1e3
# Lx = 40e3
# Ly = 11e3

# station_coord = []
# for x in range(0, int(Lx*4*1e-3)):
#     for y in range(0, int(Ly*4*1e-3)):
#         coord = (xmin + 1e3*x/4, ymin + 1e3*y/4)
#         station_coord.append(coord)
# print(len(station_coord))

