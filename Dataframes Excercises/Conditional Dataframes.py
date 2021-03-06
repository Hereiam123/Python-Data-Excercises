import numpy as np
import pandas as pd

from numpy.random import randn

# Get same random numbers predictable
np.random.seed(101)

# Create Dataframe from below values
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)

# Return boolean Dataframe where True if value at point is greater than 0
print(df > 0)

# Return values if True, NaN if False
booldf = df > 0
print(df[booldf])

# Return boolean Series
print(df['W'] > 0)

# Filter Dataframe values with boolean series
print(df[df['W'] > 0])

print(df[df['Z'] < 0])

resultdf = df[df['W'] > 0]
print(resultdf)

print(resultdf['X'])

# Stack Dataframe functionality
print(df[df['W'] > 0]['X'])
print(df[df['W'] > 0][['Y', 'X']])

# Multiple dataframe conditionals
# Won't work
#print(df[(df['W' > 0]) and (df['Y' > 1])])

# Must use (&) or (|) = ('and'/'or')
print(df[(df['W'] > 0) & (df['Y'] > 1)])
print(df[(df['W'] > 0) | (df['Y'] > 1)])

# Reset Dataframe index to numerical (non perm)
print(df.reset_index())

# Reset Dataframe to new Index (permanent)
newInd = 'CA NY WY OR CO'.split()
print(newInd)
df['States'] = newInd
print(df.set_index('States'))
