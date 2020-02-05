#Question: Write a Pandas program to convert a Panda module Series to Python list and it’s type.

import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print("Pandas Series and type: ")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list: ")
print(f"list: {ds.tolist()}")
print(type(ds.tolist()))
#