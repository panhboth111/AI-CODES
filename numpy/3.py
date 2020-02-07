# Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
arr = np.array([1,2,3,4,5])
print("Original Array is ")
print(arr)
print("Test if none of elements of array is Zero:")
print(np.all(arr))
print("-"*10)
arr = np.array([0,1,2,3,4,5])
print("Original Array is ")
print(arr)
print("Test if none of elements of array is Zero:")
print(np.all(arr))