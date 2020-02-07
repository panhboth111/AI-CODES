"""Write a Python program to change the data type of given a column or a Series.
Sample Series:
Original Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
Change the said data type to numeric:
0 100.00
1 200.00
2 NaN
3 300.12
4 400.00
dtype: float64"""
import pandas as pd
s1 = pd.Series(['100','200','python','300.12','400'])
print("Original Series")
print(s1)
print("Change the said data type to numeric")
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)