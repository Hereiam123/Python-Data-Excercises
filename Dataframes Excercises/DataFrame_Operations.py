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
