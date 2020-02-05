# Write a NumPy program to test element-wise for positive or negative infinity.
import numpy as np
ar = np.array([1, 0, np.nan, np.inf])
print("Original array: ",ar)
print("Test element-wise for positive or negative infinity:")
print(np.isinf(ar))
# print to check the boolean of the array that each element is infinity or not