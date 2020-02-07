# Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
import numpy as np
arr = np.array([1, 2, np.nan, np.inf])
print("Original Array: ")
print(arr)
print(np.isfinite(arr))