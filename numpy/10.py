# Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.

import numpy as np
x = np.array([3, 5])
y = np.array([2, 5])
print("Original numbers:")
print(x)
print(y)
print("the element in array that greater is ",np.greater(x, y))

print("the element in array that greater than or equal is: ",(np.greater_equal(x, y)))

print("the element in array that smaller than is: ", np.less(x,y))

print("the element in array that is smaller than or equal is ",np.less_equal(x,y))
