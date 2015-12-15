import numpy as np
from numpy import random
import matplotlib.pyplot as plt

x = 2*random.random(size=15**3) - 1
y = 2*random.random(size=15**3) - 1
length = np.sqrt(x**2 + y**2)
in_circle = length <= 1
plt.scatter(x[~in_circle], y[~in_circle], color="blue")
plt.scatter(x[in_circle], y[in_circle], color="red")
plt.show()

x = 2*random.random(size=10**8) - 1
y = 2*random.random(size=10**8) - 1
length = np.sqrt(x**2 + y**2)
in_circle = length <= 1
4 * in_circle.mean()

