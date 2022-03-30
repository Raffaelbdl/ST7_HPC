import matplotlib.pyplot as plt
from simulations import plots

### PATH ###
path_to_stations = "./3D_coupe/stations_3D_coupe"
simulation_name1 = "3D_pas_100m_meteo0_corr"


source2 = (14412, 16624, 00)

xs, ys, signals = plots._scatter_stations_intensity_3D(
    simulation=simulation_name1,
    path_to_stations=path_to_stations,
    norm='Inf'
)


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

ax.scatter3D(*source2, c='r', s=100, zorder=10)
ax.scatter3D(xs, ys, signals)
plt.show()