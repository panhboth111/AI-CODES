"""Question: Write a Pandas program to get the items of a given series not present in another given series. 
Sample Output:
Original Series:
sr1:
0 1
1 2
2 3
3 4
4 5
dtype: int64
sr2:
0 2
1 4
2 6
3 8
4 10
dtype: int64
Items of sr1 not present in sr2:
0 1
2 3
4 5
dtype: int64 """

import pandas as pd
sr1 = pd.Series([1, 7, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print("sr1:")
print(sr1)
print("sr2:")
print(sr2)
print("\nItems of sr1 not present in sr2:")
result = sr1[~sr1.isin(sr2)]
print(result)