import numpy as np

a = np.array([12, 3, 4, 5], dtype=int)
b = np.array([[12, 3, 4, 4], [12, 3, 4, 5], [12, 3, 4, 5], [12, 3, 4, 3]], dtype=int)

print(a + b)
print(a - b)
print(a ** 2)
print(a / 2)
print(a / b)
print(np.sqrt(a))
print(a * b)

print(np.dot(a, b))