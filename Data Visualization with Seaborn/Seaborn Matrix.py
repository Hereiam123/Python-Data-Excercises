import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())

print(flights.head())

# Need to make Dataset into a Matrix, so the index value
# represents a respective data point colum
print(tips.corr())
tc = tips.corr()

# Heatmapping data in Matrix plot
sns.heatmap(tc, annot=True, cmap='coolwarm')
# plt.show()

# Create Matrix from Flights dataframe
fp = flights.pivot_table(index='month', columns='year', values='passengers')
print(fp)

# Use line color and line width to add a little seperation in data blocks
sns.heatmap(fp, cmap='magma', linecolor='white', linewidths=1)
# plt.show()

# Cluster map, cluster columns based on similarity of data
# points. Standard scale normalizes the scale
sns.clustermap(fp, standard_scale=1)
plt.show()
