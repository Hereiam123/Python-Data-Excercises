import numpy as np
import pandas as pd

from numpy.random import randn

# Get same random numbers predictable
np.random.seed(101)

# Create Dataframe from below values
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)

# Columns
# Print Dataframe column as Series by string value of column index
print(df['W'])

# Print Dataframe column by listing value of column by dot notation
print(df.W)

# Get Multiple Columns by listed index values, returned Dataframe
print(df[['W', 'Z']])

# Create new column by gathering columns from previous Dataframe
df['new'] = df['W']+df['Y']
print(df)

# Delete column by string index value (inplace=True for permanent drop)
df.drop('new', axis=1, inplace=True)
print(df)

# Drop Row
df.drop('E', axis=0, inplace=True)
print(df)

# Get shape of Dataframe returned as Tuple
print(df.shape)

# Rows
# Get row as Series by label of Row index
print(df.loc['A'])

# Get row as Series by index value of count of Rows
print(df.iloc[2])

# Get subset value of Dataframe
print(df.loc['B', 'Y'])

# Get multiple subsets
print(df.loc[['A', 'B'], ['W', 'Y']])
