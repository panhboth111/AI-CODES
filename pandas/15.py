"""Question: Write a Pandas program to create the mean and standard deviation of the data of a given Series.
Sample Output:
Original Data Series:
0 1
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 5
10 3
dtype: int64
Mean of the said Data Series:
4.81818181818
Standard deviation of the said Data Series:
2.52262489555 """

import pandas as pd
s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print("Original Data Series:")
print(s)
print("Mean of the said Data Series:")
print(s.mean())
print("Standard deviation of the said Data Series:")
print(s.std())