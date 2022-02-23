import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

from typing import Tuple

# x = np.arange(-5.0, 5.01, 1)
# y = np.arange(-5.0, 5.01, 1)
# xx, yy = np.meshgrid(x, y)
# z = np.random.uniform(-0.1, 0.1, size=xx.shape)
# print(z.shape)

# f = interpolate.interp2d(x, y, z)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# xnew = np.arange(-5.0, 5.01, 1e-1)
# ynew = np.arange(-5.0, 5.01, 1e-1)
# xxnew, yynew = np.meshgrid(xnew, ynew)
# print(xnew, ynew)
# znew = f(xnew, ynew)
# ax.scatter3D(0.1, 0.1, f(0.1, 0.1), s=20, c='r', marker='o')
# ax.plot_wireframe(xxnew, yynew, znew)
# plt.show()

def generate_random_interpolation(min: float, max: float, step: float) -> interpolate.interp2d:

    x = np.arange(min, max, step)
    y = np.arange(min, max, step)
    xx, yy = np.meshgrid(x, y)
    z = np.random.uniform(-0.1, 0.1, size=xx.shape)

    return interpolate.interp2d(x, y, z)

def plot_random_interpolation(f: interpolate.interp2d, min: float, max: float, step: float, frac: float) -> Tuple[plt.figure, plt.axes]:
    
    xnew = np.arange(min, max, step * frac)
    ynew = np.arange(min, max, step * frac)
    xxnew, yynew = np.meshgrid(xnew, ynew)
    znew = f(xnew, ynew)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(xxnew, yynew, znew)

    return fig, ax

if __name__ == '__main__':

    min, max, step = -5., 5.01, 1
    f = generate_random_interpolation(min, max, step)
    fig, ax = plot_random_interpolation(f, min, max, step, frac = 0.5)
    plt.show() 