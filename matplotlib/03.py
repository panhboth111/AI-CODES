""" Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title.
test.txt
1 2
2 4
3 1 """

import matplotlib.pyplot as plt
with open("test.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()