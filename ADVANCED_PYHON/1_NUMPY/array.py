import numpy as np

""" numpy mac dinh tao mang so thuc """

array1d = np.array([1, 2, 3, 4]) #tạo mảng từ 1 list
print(array1d)
print(type(array1d)) #<class 'numpy.ndarray'>
print()

array2d = np.array([[1, 3, 4], [1, 3, 4]])
print(array2d)
print(type(array2d))
print()

print(array2d.shape) #cỡ của ma trận
print()

""" mảng đặt biệt """
a = np.zeros((3, 4)).astype(int) #mảng 3x4 với toàn số 0
print(a)
print()

b = np.zeros(3) #mảng 3 phần tử 0
print(b)
print()

c = np.ones(3).astype(int) #mảng toàn số 1
print(c)
print()

d = np.ones((2, 3)) #mảng 2x3 toàn số 1
print(d)
print()

e = np.full((3, 3), 7) #mảng 3x3 toàn số 7
print(e)
print()

f = np.full(3, 7) 
print(f)
print()

g = np.eye(4) #tạo ma trận đơn vị cỡ 4x4
print(g)
print()

""" tạo mảng giá trị ngẫu nhiên """
print(np.random.rand(3, 3)) #3x3 ngau nhien từ 0->1
print()

print(np.random.randint(1, 10, (2, 2))) #2x2 cac phan tu ngau nhien tu 1->10
print()

""" indexing vs slicing """
a = np.array([[1, 2, 3], [1, 2, 3]])
print(a[0, 1]) #phan tu thu 2 hang 1
print()
print(a[1, -1]) #phan tu cuoi cung cua ma tran

""" slicing """
print(a[:, 1]) #lay toan bo cot thu 2
print(a[1, :]) #lay toan bo hang thu 2
print(a[:, -1]) #lay toan bo cot cuoi cung

""" các phép toán với numpy """
print()
b = np.array([1, 2, 3, 4])
print(b * 2) #nhân tất cả phần tử của mảng với 2
print(b + 3) #cộng tất cả phần tử của mảng với 3
print(b ** 2) #bình phương tất cả phần tử của mảng

print()
c = np.array([1, 2, 3, 4])
print(b * c)
print(b + c)

