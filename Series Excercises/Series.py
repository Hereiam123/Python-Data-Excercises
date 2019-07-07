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

# Series of functions
print(pd.Series([sum, print, len]))

# Series in Variable
ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])

print(ser1)

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])

print(ser2)

print(ser1['USA'])

ser3 = pd.Series(data=labels)

print(ser3[0])

# Attempt to add Series together with unaligned values
print(ser1 + ser2)
