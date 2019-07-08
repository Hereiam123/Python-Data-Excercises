import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

# Build Dataframe from dictionary
df = pd.DataFrame(d)

print(df)

# Drop Missing dataframe based on row
print(df.dropna())

# Drop Missing dataframe based on column
print(df.dropna(axis=1))

# Don't drop Row if row contains a value of 2.0
print(df.dropna(thresh=2))

# Fills NaN values with assigned value
print(df.fillna(value='FILL VALUE'))
print(df['A'].fillna(value=df['A'].mean()))
