import numpy as np

arr = np.array([5, 56, 4], dtype=int)
print(arr)

# sort
b = np.sort(arr, kind='heapsort')
print(b)
a = np.array([[1, 3, 4], [4, 5, 1], [1, 4, 2]], dtype=int)
c = np.sort(a, axis=0, kind='quicksort') # sort theo từng cột
print(c)
d = np.sort(a, axis=1, kind='mergesort') # sort theo hàng
print(d)

# argsort: trả về chỉ số của phần tử trong mảng ban đầu sau khi sort

print(np.argsort(a, axis=0))

# argmax/argmin: trả về chỉ số của phần tử lớn nhất/nhỏ nhất trong mảng
print(np.argmax(arr)) #1
print(np.argmin(arr)) #2