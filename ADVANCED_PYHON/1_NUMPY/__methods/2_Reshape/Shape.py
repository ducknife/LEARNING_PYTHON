import numpy as np

a = np.array([[2, 3, 4], [2, 4, 3]], dtype=int)

b = a.reshape((3, 2)) # 2x3 to 3x2
print(b)

c = np.array([[12, 333, 4], [12, 3, 3], [1, 23, 4], [1, 3, 3]], dtype=int)

d = a.flatten() # nD to 1D
print(d)

d2 = c.reshape((2, 6))
print(d2)

e = a.T
print(e) # tranpose of matrix

f = np.unique(a, return_counts=True) # trả về mảng gồm các phần tử duy nhất, return_counts=True trả về mảng Fre.
print(f[0], f[1])