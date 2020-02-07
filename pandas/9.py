"""Write a Pandas program to convert a given Series to an array.
Sample Output:
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Series to an array
['100' '200' 'python' '300.12' '400']"""
import numpy as np
import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
print("Original Series")
print(s1)
print("Series to Array")
s2 = np.array(s1.values.tolist())
print(s2)