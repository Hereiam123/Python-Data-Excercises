import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

# Standard Series
print(pd.Series(data=my_data))

# Labeled index Series
print(pd.Series(data=my_data, index=labels))

# Numpy array Series
print(pd.Series(arr, labels))

# Series using Dictionary
print(pd.Series(d))

# Series of labels
print(pd.Series(labels))
