import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

# Set figure size and DPI
fig = plt.figure(figsize=(3, 2), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, y)

# Figsize Object Method
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))
axes[0].plot(x, y)
axes[1].plot(y, x)

# Tighten Layout
plt.tight_layout()

# Save figure to output file
fig.savefig('Saved Figs/my_picture.png', dpi=200)

plt.show()
