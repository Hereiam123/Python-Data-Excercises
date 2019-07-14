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

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.subplot(1, 2, 2)

plt.plot(y, x, 'b')

# Show plot
plt.show()
