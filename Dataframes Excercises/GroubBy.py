import numpy as np
import pandas as pd

data = {'Company': ['GOOG', 'GOOG', "MSFT", "MSFT", 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sale': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

print(df)

# Only prints reference in memeory to grouped dataframe
print(df.groupby('Company'))

byComp = df.groupby('Company')

# Perform functions on grouped DF
print(byComp.mean())
print(byComp.sum())
print(byComp.std())

# Get for only one row, total sum
print(byComp.sum().loc['FB'])

# Get total number of items in each column
print(byComp.count())

# Get max of values in column
print(byComp.max())

# Describe content in grouped Dataframe
print(byComp.describe())
print(byComp.describe().transpose())
