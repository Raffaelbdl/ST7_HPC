import numpy as np
import csv

# a = np.loadtxt("./3D_coupe/3D_pas_100m_meteo0_corr/TE/STATION_NOM")
# print(a)

stations = []

with open("./3D_coupe/3D_pas_100m_meteo0/TE/STATION_NOM", "r") as f:
    a = csv.reader(f, delimiter=' ')
    for row in a:
        print(row)
        if row[0][:2] == 'ST':
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
print(stations)

np.savetxt("./3D_coupe/stations_3D_coupe", stations)