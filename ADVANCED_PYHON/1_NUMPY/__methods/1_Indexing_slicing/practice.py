import numpy as np

a = np.array([1, 23, 3, 3], dtype=int)
print(a[1], a[2], a[3])
print(a[0:2])

b = np.array([[1, 3, 4, 4, 4], [1, 3, 4, 23, 3]], dtype=int)
print(b[0][0], b[0][2])

print(b[0, :])
print(b[:, 1])
print(b[:, 0:3])

print(b[b > 10])