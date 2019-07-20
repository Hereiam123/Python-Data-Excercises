import seaborn as sns
import matplotlib.pyplot as plt

# Using built in dataset
tips = sns.load_dataset('tips')

print(tips.head())

sns.distplot(tips['total_bill'])

plt.show()
