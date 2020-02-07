"""Write a Python Pandas program to convert the first column of a DataFrame as a Series.
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
1st column as a Series:
0 1
1 2
2 3
3 4
4 7
5 11
Name: col1, dtype: int64
<class 'pandas.core.series.Series'>"""
import pandas as pd
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
s1 = df.loc[df.index[:],'col1']
print("\n1st column as a Series:")
print(s1)
print(type(s1))