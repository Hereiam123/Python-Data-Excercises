import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

print(y)

# Plot out data points
plt.plot(x, y)

# Add X, Y label and Title of plot
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')

# Multiple subplots
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')

# Object oriented plot intro
fig = plt.figure()

# Setting axes values
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Plotting data on axes
axes.plot(x, y)
axes.set_xlabel('X Label')
axes.set_ylabel('Y Label')
axes.set_title('Set Title')

# Show plots
plt.show()
