import seaborn as sns
import matplotlib.pyplot as plt


# Measurement of different flowers
iris = sns.load_dataset('iris')
print(iris.head())


g = sns.PairGrid(iris)
# Plot a scatter plot on the created grid
# g.map(plt.scatter)

# Plot dist plots on grid
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

plt.show()
