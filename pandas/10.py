"""Write a Pandas program to convert Series of lists to one Series.
Sample Output:
Original Series of list
0 [Red, Green, White]
1 [Red, Black]
2 [Yellow]
dtype: object
One Series
0 Red
1 Green
2 White
3 Red
4 Black
5 Yellow
dtype: object"""
import pandas as pd
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print(s)