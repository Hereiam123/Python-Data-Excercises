import seaborn as sns
import matplotlib.pyplot as plt


# Measurement of different flowers
iris = sns.load_dataset('iris')
print(iris.head())


# Pair Grid
g = sns.PairGrid(iris)
# Plot a scatter plot on the created grid
# g.map(plt.scatter)

# Plot dist plots on grid
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

plt.show()

# Facet Grid
# Able to map datapoints, but based on column names
# And mapping on what you want to display
tips = sns.load_dataset('tips')
g = sns.FacetGrid(tips, col='time', row='smoker')
g.map(sns.distplot, 'total_bill')
plt.show()
