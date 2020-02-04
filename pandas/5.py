import pandas as pd
fruits = {'apple':'$1','banana':'$1','orange':'$1'}
print(f"original dictionary: {fruits}")
ds = pd.Series(fruits)
print(ds)