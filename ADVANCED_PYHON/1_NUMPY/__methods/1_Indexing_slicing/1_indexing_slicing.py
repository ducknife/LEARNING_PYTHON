import numpy as np

a = np.array([2, 3, 3, 3, 4], dtype=int)
print(a[-1])

a2 = np.array([[2, 3, 34, 4], [12, 3, 3, 2]], dtype=int)
print(a2[1, 3])

print(a2[:, 1]) # lấy cột 1
print(a2[1, :]) # lấy hàng 1
print(a2[0:2, 0:1]) # lấy hàng 0->1, cột 0->0 #output: [[2][12]]

# lọc điều kiện
print(a2[a2 > 10]) # 34 12
print(a[a > 3])