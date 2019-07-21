import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Show a linear reg line
# Add markers for division icons on hue
# Scatter kws allows changing of marker size
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex',
           markers=['o', 'v'], scatter_kws={'s': 100})

plt.show()
