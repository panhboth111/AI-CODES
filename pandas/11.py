# Write a Pandas program to sort a given Series.

import pandas as pd
s = pd.Series(['50', '15', 'python', '30.45', '400'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print("Data that sorted is: ",new_s)