import numpy as np

#numpy array
a = np.array([1, 4, 4, 5], dtype=int) # create 1D array.
print(a)

b = np.array([[123, 123], [123, 213]], dtype=float) # create 2D array
print(b)

c = np.zeros((2, 3), dtype=int) # matrix 2 x 3 contains full of zeros.
print(c)
 
d = np.ones((2, 3), dtype=int) # matrix 2 x 3 contains full of ones.
print(d)

e = np.eye(3, dtype=int) # create identity matrix size N, can be rectangle. EXP eye(3, 2, dtype=int)
print(e)

f = np.identity(3, dtype=int) # create identity matrix size N, only square. 
print(f)

f1 = np.full((2, 3), 3, dtype=int) # create matrix with all value is 3.
print(f1)

""" tham khảo thêm """

g = np.arange(0, 11, 2, dtype=int) # create array 1D with num in range(start, stop, step)
print(g)
h = np.linspace(0, 10, 50, endpoint=False, dtype=int) # create array 1D with 50 elements, endpoint=True means use stop.
print(h) # các phần tử chia đều. 
i = np.random.rand(2, 4) # matrix 2 x 4 with all elements in range [0, 1)
print(i)
j = np.random.randn(2, 4) # matrix 2 x 4 with gauss 
print(j)
SIZE = 10
k = np.random.randint(0, 10, SIZE, dtype=int) # create array 1D with elements in range [a, b)
print(k)

""" attribute """
print(j.ndim) #in ra số chiều của mảng.

print(j.size) #in ra tổng số phần tử của mảng.

print(j.shape) #in ra số hàng x số cột theo 1 tuple.

print(j.dtype) #in ra kiểu dữ liệu của mảng.
