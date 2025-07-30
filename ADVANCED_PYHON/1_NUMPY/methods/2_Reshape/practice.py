import numpy as np

a = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]], dtype=int)

b = a.reshape((5, 3))
c = a.flatten()
d = a.T
e = np.unique(a, return_counts=True)

print("Reshape a from 3x5 to 5x3:\n", b)
print("Flatten a from 2D to 1D:\n", c)
print("Tranpose matrix of a:\n", d)
print("different elements in a:\n", e[0])
print("frequences of elements in a:\n", e[1])