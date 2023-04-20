import numpy as np

print("Implementation of Least Square Method in NumPy: ")

A = np.array([1,2,1,1,1,2,2,1,1])

print("\nThe Array A is: ", A)

B = np.array([4,3,5,4,2,3,6,3,2])

print("\nThe Array B is: ", B)
# Stack arrays in sequence vertically (row wise). rcond is used to zero out small entries in D.
X = np.linalg.lstsq(np.vstack([A, np.ones(len(A))]).T, B, rcond=None)[0]
 
print("\nThe Least Square is: ", X)