import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})
# Return rows
print(df.head())

# Return unique values
print(df['col2'].unique())

# Count of Unique values
print(df['col2'].nunique())

# Count of unique values, by values
print(df['col2'].value_counts())

# Select data in Dataframe conditionally
print(df[(df['col1'] > 2) & (df['col2'] == 444)])


def times2(x):
    return x*2


# Apply function to each element in each column
print(df['col1'].apply(times2))

print(df['col3'].apply(len))

# Using lambda functions
print(df['col2'].apply(lambda x: x*2))

# Remove column based on column specification
#print(df.drop('col1', axis=1, inplace=True))

# Call out dataframe column names
print(df.columns)

# Call out index values
print(df.index)

# Sort values based on column value
print(df.sort_values('col2'))

# Check if any element is null
print(df.isnull())

# Working with pivot tables
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)

print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))
