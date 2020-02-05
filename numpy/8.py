# Write a NumPy program to test element-wise for complex number, real number of a given array. Also test if a given number is a scalar type or not.

import numpy as np
ar = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("The given array is: ",ar)

print("Check for complex number: ",np.iscomplex(ar))

print("Check for real number:",np.isreal(ar))

print("Check for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([5.3]))