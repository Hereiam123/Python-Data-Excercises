import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

print(y)

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

# Add legend to plot with labels
ax.plot(x, x**2, label='X Squared')
ax.plot(x, x**3, label='X Cubed')
ax.legend()

plt.show()
