import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax2 = fig.add_axes([0, 0, 1, 1])


# Set line color with basic color syntax
ax.plot(x, y, color='orange')

# Using RGB values
ax.plot(x, y, color="#FF8C00")

# Setting line width against default width
# Setting line alpha value (transparency)
# Setting line style
# Setting marker to reveal data points for plot
# Setting marker size
# Setting marker color
# Setting marker edge width and color
ax2.plot(y, x, color="purple", linewidth=3,
         alpha=0.5, linestyle='-', marker='o', markersize=20, markerfacecolor='yellow', markeredgewidth=3, markeredgecolor="green")

plt.show()
