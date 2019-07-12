import numpy as np
import pandas as pd
from numpy.random import randn

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(outside)
print(inside)
print(hier_index)

# Construct Multilayer index Dataframe
df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)

# Retrieve values from Multilayer Dataframe
print(df.loc['G1'])
# Deeper index
print(df.loc['G1'].loc[1])

# Give Multiplayer index columns names
df.index.names = ['Groups', 'Num']
print(df)
print(df.index.names)

print(df.loc['G2'].loc[2]['B'])

# Cross sections
print(df.xs('G1'))
print(df.xs(1, level='Num'))
