import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0,1,200)

def f(x):
    return 1/(1+np.exp(10*(0.35-x)))

Y= f(X)-f(0)

plt.plot(X,Y, color="r")
plt.plot(X,X, color = "blue")
plt.show()
