import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# Aggregate Categorical Data via a specific method, average by default
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

# Count plot, estimator is specifically number of occurences
sns.countplot(x='sex', data=tips)

# Box plot, shows distribution of categorical data
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

# Violin Plots, similar to boxplot
# Show distribution of data across a category
sns.violinplot(x='day', y='total_bill', data=tips)


plt.show()
