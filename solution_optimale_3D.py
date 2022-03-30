import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
from simulations import plots


path_to_te = "./3D_coupe/3D_pas_100m_meteo0_corr/TE/"
path_to_te1 = "./3D_coupe/3D_pas_100m_meteo1_corr/TE/"
path_to_te2 = "./3D_coupe/3D_pas_100m_meteo2_corr/TE/"
path_to_stations = "./3D_coupe/stations_3D_coupe"
stations = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]
stations1 = [s for s in os.listdir(path_to_te1) if "STATION_ST" in s]
stations2 = [s for s in os.listdir(path_to_te2) if "STATION_ST" in s]
num_stations = len(stations)
num_stations1 = len(stations1)
num_stations2 = len(stations2)
x_source = 14412
y_source = 16624
z_source = 1900
exclusion_zone =10000 # rayon de la zone interdite

## stations_irl = np.loadtxt("stations_2D_coupe_1")

intensities, intensities1, intensities2 = [], [], []
intensities_wout, intensities_wout1, intensities_wout2 = [], [], []

ids, ids1, ids2= [], [], []


##########################################
        #CHARGEMENT DES DONNÉES# 
##########################################
print("loading data ...")
stations_irl = np.loadtxt(path_to_stations)
station_pos = {}
for station_irl in stations_irl :
    station_pos[int(station_irl[3])] = {"x": station_irl[0], "y": station_irl[1], "z": station_irl[2]}

############# PAS DE VENT ################
print("loading no wind ...")
dico_int={}
for station in stations:
    array = np.loadtxt(open(os.path.join(path_to_te, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    ## print(non_nul)
    # valeur efficace
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))
    
    #on met tout dans un dico qui classe tout 
    dico_int[station[10:]] = intensitiy_wout

intensities = dico_int



########## METEO1 ##############
print("loading upwind ...")
dico_int={}
for station in stations1:
    array = np.loadtxt(open(os.path.join(path_to_te1, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    dico_int[station[10:]] = intensitiy_wout

intensities1 = dico_int



############# METEO 2 ####################
print("loading downwind ...")
dico_int={}
for station in stations2:
    array = np.loadtxt(open(os.path.join(path_to_te2, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    dico_int[station[10:]] = intensitiy_wout

intensities2 = dico_int


##########################################
        #PROCESSING DES DONNÉES# 
##########################################
print("cleaning data ...")

# On place une zone interdite autour de la source

forbiden_station = set()#set des balises à exclure
exclusion_zone = exclusion_zone**2
for station_irl in station_pos:
    distance_eucli = (x_source - station_pos[station_irl]['x'])**2 + (y_source - station_pos[station_irl]['y'])**2
    if (distance_eucli < exclusion_zone) :
            forbiden_station.add(str(station_irl))


intensities_key = set(intensities.keys())
intensities1_key = set(intensities1.keys())
intensities2_key = set(intensities2.keys())
for station_num in forbiden_station:
    if station_num in intensities_key:
        intensities.pop(station_num)
    if station_num in intensities1_key:
        intensities1.pop(station_num)
    if station_num in intensities2_key:
        intensities2.pop(station_num)

# Première approche
def f(x):
    return 1/(1+np.exp(10*(0.35-x)))

# on normalise les données
intensities_value = intensities.values()
max_inten = max(intensities_value)
min_inten = min(intensities_value)
for key in intensities :
    intensities[key] = f((intensities[key] - min_inten)/(max_inten - min_inten)) - f(0)

intensities_value = intensities1.values()
max_inten = max(intensities_value)
min_inten = min(intensities_value)
for key in intensities1 :
    intensities1[key] = f((intensities1[key] - min_inten)/(max_inten - min_inten)) - f(0)

intensities_value = intensities2.values()
max_inten = max(intensities_value)
min_inten = min(intensities_value)
for key in intensities2 :
    intensities2[key] = f((intensities2[key] - min_inten)/(max_inten - min_inten)) - f(0)


#on trouve la meileur balise
print("looking for best station ...")
sum_sol = {}
current_max = 0
for key in intensities.keys():
    sum_sol[key] = intensities[key] + intensities1[key] + intensities2[key]
    if sum_sol[key] > current_max : 
        current_max = sum_sol[key]
        best_bal = int(key)

########## Plot Results ##########

print("plotting result ...")
### GET RELIEF ###
x_relief, y_relief, z_relief = plots._relief3D()
relief_kwargs = {
    'antialiased': True,
    'cmap': 'terrain',
}

fig, ax = plots.plot_relief3D(**{
    'antialiased': True,
    'cmap': 'terrain',
})
ax.scatter3D(x_source, y_source, z_source, color = "red")
ax.scatter3D(station_pos[best_bal]["x"],station_pos[best_bal]["y"],station_pos[best_bal]["z"], color = "k")
plt.show()