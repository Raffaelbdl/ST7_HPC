from metaheuristics.simulated_annealing import simulated_annealing, neighborhood_disk, evaluate_pos2d
from generate_function import generate_random_interpolation, plot_random_interpolation
import numpy as np
import matplotlib.pyplot as plt
from functools import partial

min, max, step = -5., 5.01, 0.5
clips = np.array([[min, max], [min, max]])

f = generate_random_interpolation(min, max, step)

energy_fn = partial(evaluate_pos2d, f_2d=f)
neighborhood_fn = neighborhood_disk

best_pos, best_energy = simulated_annealing(100000, neighborhood_fn, energy_fn, clips, 10)
print(best_pos, best_energy)

fig, ax = plot_random_interpolation(f, min, max, step, 0.5)
ax.scatter3D(best_pos[0], best_pos[1], best_energy, marker='o', c='r', s=10)
plt.show()