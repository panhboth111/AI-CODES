"""Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series. 
Sample Output:
Original Series:
0 3.000938
1 11.370722
2 14.612143
3 8.990256
4 13.925283
5 12.056875
.... 17 14.118931
18 8.247458
19 5.526727
dtype: float64
Minimum, 25th percentile, median, 75th, and maximum of a given series:
[ 3.00093811 8.09463867 10.23353705 12.21537733 14.61214321] """

import pandas as pd
import numpy as np
num_state = np.random.RandomState(100)
num_series = pd.Series(num_state.normal(10, 4, 20))
print("Original Series:")
print(num_series)
result = np.percentile(num_series, q=[0, 25, 50, 75, 100])
print("\nMinimum, 25th percentile, median, 75th, and maximum of a given series:")
print(result)