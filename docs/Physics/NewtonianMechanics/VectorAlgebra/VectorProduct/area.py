import numpy as np

A = np.array([3, 2, 0])
B = np.array([1, 4, 0])
C = np.cross(A, B)
area = np.linalg.norm(C)
print("Area =", area)