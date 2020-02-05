#Question: Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title. 

import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,1]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()
