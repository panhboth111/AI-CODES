# Write a NumPy program to test element-wise for NaN of a given array.
import numpy as np
ar = np.array([np.nan, np.inf, 10, 20])
print("The given Array: ",ar)
print("Test element-wise for Nan: ",np.isnan(ar))