from metaheuristics.simulated_annealing import simulated_annealing, neighborhood_disk, evaluate_pos2d, linear_temp_decay
from generate_function import generate_random_interpolation, plot_random_interpolation
import numpy as np
import matplotlib.pyplot as plt
from functools import partial

min, max, step = -10., 10.01, 1
clips = np.array([[min, max], [min, max]])

# with 2 artificial minimas
f, f_min = generate_random_interpolation(min, max, step)

energy_fn = partial(evaluate_pos2d, f_2d=f)
neighborhood_fn = neighborhood_disk
temperature_decay = partial(linear_temp_decay, alpha=0.99, min_temperature=1)

best_pos, best_energy = simulated_annealing(100000, neighborhood_fn, energy_fn, clips, 100, temperature_decay)
print("best energy annealing ", best_energy) 

fig, ax = plot_random_interpolation(f, min, max, step, 0.5)
ax.scatter3D(best_pos[0], best_pos[1], best_energy, marker='o', c='r', s=10)
print("minimum ", f_min)
print("error ", f_min - best_energy)
plt.show()