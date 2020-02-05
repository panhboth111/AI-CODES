"""Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series. Go to the editor
Sample Output:
Original Series:
0 4
1 3
2 4
3 3
4 4
5 1
... 13 2
14 1
dtype: int64
Top 2 Freq: 4 5
3 4
2 3
1 3
dtype: int64 """

import pandas as pd
import numpy as np
<<<<<<< HEAD
np.random.RandomState(100)
=======
>>>>>>> borey
num_series = pd.Series(np.random.randint(1, 5, [15]))
print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
<<<<<<< HEAD
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
=======
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'
>>>>>>> borey
