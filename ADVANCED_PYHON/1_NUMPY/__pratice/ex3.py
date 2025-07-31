import numpy as np

""" giai phuong trinh Ax = b """

A = np.array([[4, 7], [2, 6]], dtype=int)

b = np.array([8, 10], dtype=int)

# cách 1:
print(np.linalg.solve(A, b)) # A phải khả nghịch 

# cách 2:
AInv = np.linalg.inv(A)

x = np.dot(AInv, b)

print(x)

# bổ sung kiến thức:
# 1. Tính định thức
print(np.linalg.det(A))

# 2. Tính nghịch đảo ma trận
print(np.linalg.inv(A))
