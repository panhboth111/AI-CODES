#Question: Write a Python program to add, subtract, multiple and divide two Pandas Series
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
print("Data series 1:")
print(ds1)
print("Data series 2:")
print(ds2)
print("ADDITION:")
print(ds1+ds2)
print("SUBSTRACTION: ")
print(ds1-ds2)
print("MULTIPLICATION:")
print(ds1*ds2)
print("DIVISION:")
print(ds1/ds2)
#