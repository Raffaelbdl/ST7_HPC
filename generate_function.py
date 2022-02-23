import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.arange(-5.0, 5.01, 1)
y = np.arange(-5.0, 5.01, 1)
xx, yy = np.meshgrid(x, y)
z = np.random.uniform(-0.1, 0.1, size=xx.shape)
print(z.shape)

f = interpolate.interp2d(x, y, z)

fig = plt.figure()
ax = plt.axes(projection='3d')
xnew = np.arange(-5.0, 5.01, 1e-1)
ynew = np.arange(-5.0, 5.01, 1e-1)
xxnew, yynew = np.meshgrid(xnew, ynew)
print(xnew, ynew)
znew = f(xnew, ynew)
ax.scatter3D(0.1, 0.1, f(0.1, 0.1), s=20, c='r', marker='o')
ax.plot_wireframe(xxnew, yynew, znew)
plt.show()