import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])

# Set line color with basic color syntax
ax.plot(x, y, color='orange')

# Using RGB values
ax.plot(x, y, color="#FF8C00")
