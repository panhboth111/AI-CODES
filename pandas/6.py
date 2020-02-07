"""Write a Python program to convert a NumPy array to a Pandas series.
Sample Series:
NumPy array:
[10 20 30 40 50]
Converted Pandas series:
0 10
1 20
2 30
3 40
4 50
dtype: int64"""
import numpy as np
import pandas as pd
np_array = np.array([10,20,30,40,50])
print("Original numpy Array")
print(np_array)
new_series = pd.Series(np_array)
print(new_series)