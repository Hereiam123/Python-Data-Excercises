import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('CSV Content/df1', index_col=0)
df2 = pd.read_csv('CSV Content/df2')

print(df1)
print(df2)

# Plot data to histogram
df1['A'].hist(bins=30)
plt.show()

# Plot with kind or plot directly
df1['A'].plot(kind='hist', bins=30)
plt.show()

df1['A'].plot.hist(bins=30)
plt.show()

# Area plot with some transparency
df2.plot.area(alpha=0.5)
plt.show()

# Bar plot, stacking values
df2.plot.bar(stacked=True)
plt.show()

# Line plots
# df1.plot.line(x=df1.index, y='B', figsize=(12, 3), lw=1)
# plt.show()

# Scatter plot
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')
plt.show()

# Box plot
df2.plot.box()
plt.show()

# Hexagonal plot
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
print(df.head())
df.plot.hexbin(x='a', y='b', gridsize=25)
plt.show()

# Kernel Density information plot
df2['a'].plot.kde()
plt.show()
