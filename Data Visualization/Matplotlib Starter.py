import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(0, 5, 11)
y = x**2

print(y)

# Plot out data points
plt.plot(x, y)

# Show plot
plt.show()
