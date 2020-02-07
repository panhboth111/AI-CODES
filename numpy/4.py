# Write a NumPy program to test if any of the elements of a given array is non-zero.
import numpy as np
arr = np.array([1,0,0,0])
print("Original Array is ")
print(arr)
print("Test if none of elements of array is non-Zero:")
print(np.any(arr))
print("-"*10)
arr = np.array([0,0,0,0])
print("Original Array is ")
print(arr)
print("Test if none of elements of array is non-Zero:")
print(np.any(arr))