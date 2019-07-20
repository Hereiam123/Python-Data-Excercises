import seaborn as sns
import matplotlib.pyplot as plt

# Using built in dataset
tips = sns.load_dataset('tips')

print(tips.head())

# Removing kernel density information(kde)
sns.distplot(tips['total_bill'], kde=False, bins=30)

# Combine two distplots by variant
# Comparing total_bill value and tips
# Hex kind value changes points from sctatterpot dots
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')

# Regression line added
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')

# Kde will show density within joint values
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')

# Pair plot will act as a jointplot across all numerical columns
# In a dataframe

# Hue will allow string values in a column to be plotted
# Based on listed column
sns.pairplot(tips, hue='sex', palette='coolwarm')

# Rugplot draws dashed plot of datapoint listed in column
# Below
sns.rugplot(tips['total_bill'])


plt.show()
