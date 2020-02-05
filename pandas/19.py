"""Write a Pandas program to calculate the frequency counts of each unique value of a given series. 
Sample Output:
Original Series:
0 1
1 7
2 1
3 6
4 9
5 1
... 29 2
30 9
31 1
32 2
33 9
34 2
35 9
36 0
37 0
38 4
39 8
dtype: object
Frequency of each unique value of the said series.
0 9
2 7
9 6
1 5
6 3
8 3
7 3
3 2
4 1
5 1
dtype: int64 """

import pandas as pd
import numpy as np
num_series = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
print("Original Series:")
print(num_series)
print("Frequency of each unique value of the said series.")
result = num_series.value_counts()
print(result)