import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

from typing import Tuple

def generate_random_interpolation(min: float, max: float, step: float) -> interpolate.interp2d:

    x = np.arange(min, max, step)
    y = np.arange(min, max, step)
    xx, yy = np.meshgrid(x, y)
    z = np.random.uniform(-0.1, 0.1, size=xx.shape)

    z[np.random.randint(len(x))][np.random.randint(len(y))] = -1.4
    z[np.random.randint(len(x))][np.random.randint(len(y))] = -1

    return interpolate.interp2d(x, y, z), np.min(z)

def generate_sinusoidal_interpolation(
    intensity: float,
    period: float,
    offset: float,
    min: float, 
    max: float, 
    step: float
) -> interpolate.interp2d:

    x = np.arange(min, max, step)
    y = np.arange(min, max, step)
    xx, yy = np.meshgrid(x, y)
    z = np.sin(np.sqrt(xx**2 + yy**2) * 2 * np.pi / period + offset) / (np.sqrt(xx**2 + yy**2))

    return interpolate.interp2d(x, y, z), -intensity

def plot_interpolation(f: interpolate.interp2d, min: float, max: float, step: float, frac: float) -> Tuple[plt.figure, plt.axes]:
    
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
    fig, ax = plot_interpolation(f, min, max, step, frac = 0.5)
    plt.show() 