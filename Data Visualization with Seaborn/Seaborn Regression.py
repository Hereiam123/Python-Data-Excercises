import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Show a linear reg line
# Add markers for division icons on hue
# Scatter kws allows changing of marker size
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex',
           markers=['o', 'v'], scatter_kws={'s': 100})

plt.show()

# Vary plot by column value, and row value
# Similar to grids
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex', row='time')

plt.show()

# Add a little more variation based on hue
# Change aspect ratio of gridded plots
sns.lmplot(x='total_bill', y='tip', data=tips,
           col='day', hue='sex', aspect=0.6, height=8)

plt.show()
