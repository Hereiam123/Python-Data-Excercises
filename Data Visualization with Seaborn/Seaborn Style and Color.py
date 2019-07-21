import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Set style for plot background
# E.g. 'black','whitegrid', 'greygrid'
sns.set_style('whitegrid')
sns.countplot(x='sex', data=tips)
plt.show()

# Set style for ticks
sns.set_style('ticks')
sns.countplot(x='sex', data=tips)

# Remove spines from plot
# Right and top by default
sns.despine(left=True, bottom=True)
plt.show()

# Adjust overall figure size
plt.figure(figsize=(12, 3))
sns.countplot(x='sex', data=tips)
plt.show()

# Adjust figure size based on context of
# intended display
sns.set_context(context='poster', font_scale=2)
sns.countplot(x='sex', data=tips)
plt.show()

# Adjusting color styling
# with Palette argument
sns.set_context(context='notebook', font_scale=1)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')
plt.show()

sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='seismic')
plt.show()
