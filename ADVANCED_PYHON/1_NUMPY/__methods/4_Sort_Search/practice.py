import numpy as np

arr = np.array([[12, 3, 3], [123, 3, 3]], dtype=int)

print(np.sort(arr, kind='heapsort'))
print(np.argsort(arr))
print(np.argmin(arr))
print(np.argmax(arr))