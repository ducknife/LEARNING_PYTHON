import numpy as np

arr = np.array([[2, 3, 4], [4, 5, 1]], dtype=int)

arr2 = np.array([[2, 3, 4], [4, 5, 1]], dtype=int)

print(arr + arr2) # cộng theo vị trí tương ứng
print(arr - arr2) # trừ theo vị trí tương ứng
print(arr ** 2) # bình phương tất cả phần tử của ma trận
print(arr * arr2) # nhân tất cả phần tử ma trận 1 với ma trận 2 theo vị trí tương ứng

arr3 = np.array([[3, 2, 1], [3, 3, 3], [1, 2, 3]], dtype=int)
print(np.dot(arr, arr3)) # tính tích vô hướng hoặc nhân 2 ma trận
