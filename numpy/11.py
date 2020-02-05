#Question:Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
import numpy as np 
a = np.array([1,2,3,4,5,6,7,8,9,10])
b = np.array([1,2,3,4,5,6,7,8,9,11])
print("Orginal arrays: ")
print(a)
print(b)
print(np.equal(a,b))
print(np.allclose(a,b))
