import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,12000,500)

def f(x):
    return min(x/10000,1)
Y= np.zeros(500)
for i in range(len(Y)):
    Y[i] = f(X[i])

plt.plot(X,Y, color="r")

plt.show()
