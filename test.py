from os import stat
from tqdm import tqdm
import json


xmin = -10e3
ymin = 1e3
Lx = 40e3
Ly = 11e3

station_coord = []
for x in range(0, int(Lx*4*1e-3)):
    for y in range(0, int(Ly*4*1e-3)):
        coord = (xmin + 1e3*x/4, ymin + 1e3*y/4)
        station_coord.append(coord)
print(len(station_coord))
json.dump(station_coord, open("station_500m.json", "w"))