import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# Aggregate Categorical Data via a specific method, average by default
#sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

# Count plot, estimator is specifically number of occurences
#sns.countplot(x='sex', data=tips)

# Box plot, shows distribution of categorical data
#sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

# Violin Plots, similar to boxplot
# Show distribution of data across a category
#sns.violinplot(x='day', y='total_bill', data=tips, hue='sex', split=True)

# Draws scatterplot, where one variable is categorical
# Jitter helps to differentiate very similar, possibly stacked poiints
# sns.stripplot(x='day', y='total_bill', data=tips,
#             jitter=True, hue='sex', split=True)

# Combining Violin above with Swarm below to show
# Overall similarity between visual presentation
#sns.swarmplot(x='day', y='total_bill', data=tips, color='black')

# Good for group comparison
sns.factorplot(x='day', y='total_bill', data=tips, kind='bar')

plt.show()
