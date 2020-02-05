#Question: Write a NumPy program to find the number of rows and columns of a given matrix.
import numpy as np
m= np.arange(10,22).reshape((3, 4))
print("MATRIX:")
print(m)
print(f" rows:{m.shape[0]}")
print(f" columns:{m.shape[1]}")
#