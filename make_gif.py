import os

import matplotlib.pyplot as plt
import numpy as np
import imageio
from tqdm import tqdm
from utils import generate_stations, plots


### 2D GIF ### 

# stations_coords = generate_stations.make_stations()
# init_stations_y = 9e3 * np.ones_like(stations_coords[..., 1]) 
# relief = plots._relief()

# num_ite = 100
# step = 100
# for k in range(num_ite):
#     stations_y = np.maximum(stations_coords[..., 1], init_stations_y - step * k)
#     fig, ax = plt.subplots()
#     ax.plot(relief[0], relief[1], c='k', alpha=0.4)
#     ax.scatter(stations_coords[..., 0], stations_y, c='g', s=25)
#     ax.set_ylim([1000, 9000])
#     plt.savefig(f"./gifs/png_{k}")
#     plt.close()

### 3D GIF ###

# stations_coords = generate_stations.make_stations_3D()
# init_stations_z = 9e3 * np.ones_like(stations_coords[..., 2])

# num_ite = 200
# step = 50
# step_az = 5
# azimuts = np.linspace(5 * 36, 261, num=num_ite)
# for k in range(num_ite):
#     stations_z = np.maximum(stations_coords[..., 2], init_stations_z - step * k)  

#     fig, ax, _ = plots.plot_relief3D(cmap='terrain', antialiased=True)
#     ax.view_init(30, azimuts[k])
#     ax.scatter3D(
#         stations_coords[..., 0], 
#         stations_coords[..., 1], 
#         stations_z,
#         c='g', s=5)
#     ax.set_zlim([1000, 9000])
#     plt.savefig(f"./gifs_3D/{k}", dpi=100)
#     plt.close()


# listdir = [str(a) + ".png" for a in sorted(int(c[:-4]) for c in os.listdir("./gifs_3D/"))]
# iterator = tqdm(listdir)
# with imageio.get_writer("gif_3D.gif", mode='I') as writer:
#     for filename in iterator:
#         image = imageio.imread(os.path.join("./gifs_3D/", filename))
#         writer.append_data(image)


listdir = ["png_" + str(a) + ".png" for a in sorted(int(c[:-4][4:]) for c in os.listdir("./gifs_2D/"))]
iterator = tqdm(listdir)
with imageio.get_writer("gif_2D.gif", mode='I') as writer:
    for filename in iterator:
        image = imageio.imread(os.path.join("./gifs_2D/", filename))
        writer.append_data(image)