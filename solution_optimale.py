import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import os

path_to_te1 = "./2D_coupe/2D_coupe_meteo1/TE/"
path_to_te2 = "./2D_coupe/2D_coupe_meteo2/TE/"
path_to_te = "./2D_coupe/2D_coupe_hors_sol/TE/"
stations = [s for s in os.listdir(path_to_te) if "STATION_ST" in s]
stations1 = [s for s in os.listdir(path_to_te1) if "STATION_ST" in s]
stations2 = [s for s in os.listdir(path_to_te2) if "STATION_ST" in s]
num_stations = len(stations)
num_stations1 = len(stations1)
num_stations2 = len(stations2)

## stations_irl = np.loadtxt("stations_2D_coupe_1")

intensities, intensities1, intensities2 = [], [], []
intensities_wout, intensities_wout1, intensities_wout2 = [], [], []

ids, ids1, ids2= [], [], []


##########################################
        #CHARGEMENT DES DONNÉES# 
##########################################

############# PAS DE VENT ################
dico_int={}
for station in stations:
    array = np.loadtxt(open(os.path.join(path_to_te, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensity = np.sqrt(np.mean(np.square(_array[non_nul:])))
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))
    
    #on met tout dans un dico qui classe tout 
    dico_int[station[10:]] = intensitiy_wout

#on met toutes les valeures stockées dans la liste des intensitées
numList=[]
for num in list(dico_int.keys()):
    numList.append(int(num))
for num in sorted(numList):
    intensities.append(dico_int[str(num)])


########## METEO1 ##############

dico_int={}
for station in stations1:
    array = np.loadtxt(open(os.path.join(path_to_te1, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensity = np.sqrt(np.mean(np.square(_array[non_nul:])))
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    dico_int[station[10:]] = intensitiy_wout

#on met toutes les valeures stockées dans la liste des intensitées
numList=[]
for num in list(dico_int.keys()):
    numList.append(int(num))
for num in sorted(numList):
    intensities1.append(dico_int[str(num)])



############# METEO 2 ####################
dico_int={}
for station in stations2:
    array = np.loadtxt(open(os.path.join(path_to_te2, station)))
    _array = array[..., 1] - 1e5
   ## print(np.where(_array != 0)[0])
    non_nul = np.min(np.where(_array != 0)[0])
    ## print(non_nul)

    # valeur efficace
    intensity = np.sqrt(np.mean(np.square(_array[non_nul:])))
    intensitiy_wout = np.sqrt(np.mean(np.square(array[..., 1] - 1e5)))

    dico_int[station[10:]] = intensitiy_wout

#on met toutes les valeures stockées dans la liste des intensitées
numList=[]
for num in list(dico_int.keys()):
    numList.append(int(num))
for num in sorted(numList):
    intensities2.append(dico_int[str(num)])


##########################################
        #PROCESSING DES DONNÉES# 
##########################################

# On place une zone interdite autour de la source

intensities = intensities[:51]+intensities[69:]
intensities1= intensities1[:51]+intensities1[69:]
intensities2 = intensities2[:51]+intensities2[69:]

# on normalise les données
intensities = (intensities - np.min(intensities))
intensities = intensities/np.max(intensities)
intensities1 = (intensities1 - np.min(intensities1))
intensities1 = intensities1/np.max(intensities1)
intensities2 = (intensities2 - np.min(intensities2))
intensities2 = intensities2/np.max(intensities2)

# Première approche
def f(x):
    return 1/(1+np.exp(10*(0.35-x)))


intensities_sol1 = f(intensities) - f(0)
intensities1_sol1 = f(intensities1) - f(0)
intensities2_sol1 = f(intensities2) - f(0)

"""
plt.plot(intensities, color = "r")
plt.plot(intensities_sol1)
plt.show()

plt.plot(intensities1_sol1)
plt.plot(intensities1, color = "r")
plt.show()

plt.plot(intensities2_sol1)
plt.plot(intensities2, color = "r")
plt.show()

plt.plot(intensities_sol1, color = "r")
plt.plot(intensities1_sol1, color = "g")
plt.plot(intensities2, color = "b")
plt.show()
"""

sum_sol_correct = intensities1_sol1 + intensities2_sol1 + intensities_sol1
sum_sol_correct = np.concatenate((sum_sol_correct[:51], [0]*18, sum_sol_correct[51:]))
intensities = np.concatenate((intensities[:51], [0]*18, intensities[51:]))
intensities1 = np.concatenate((intensities1[:51], [0]*18, intensities1[51:]))
intensities2 = np.concatenate((intensities2[:51], [0]*18, intensities2[51:]))


plt.plot(sum_sol_correct, color ="k", label = "somme")
plt.plot(intensities, color = "r", alpha = 0.5, label = "pas de vent")
plt.plot(intensities1, color = "g", alpha = 0.5, label = "meteo 1")
plt.plot(intensities2, color = "b", alpha = 0.5, label = "meteo 2")
plt.legend()
plt.show()

best_index = np.where(sum_sol_correct == np.max(sum_sol_correct))[0][0]
stations_irl = np.loadtxt("stations_2D_coupe_1")


with open("./2D_coupe/topoIS_2D_ymax.dat", "r") as f:
    topology = np.loadtxt(f)
relief = topology[...,2]
# x = np.arange(len(relief))
x = topology[..., 0]

x_source = 19382
y_source = 4290

xBest = stations_irl[best_index+5][1]
yBest = stations_irl[best_index+5][2]


plt.plot(x, relief, color = "blue")
plt.plot([stations_irl[51+5][1],stations_irl[51+5][1],stations_irl[68+5][1], stations_irl[68+5][1], stations_irl[51+5][1]],[1000, 6000, 6000, 1000, 1000], color = "y", alpha = 0.5 )
plt.scatter(x_source, y_source, c='r', s=100)
plt.scatter(xBest, yBest, c='g', s=100)
plt.show()