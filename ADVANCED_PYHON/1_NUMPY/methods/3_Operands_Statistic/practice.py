import numpy as np

arr = np.array([[213, 3, 3, 3], [23, 3, 3, 3], [123, 4, 4, 5]], dtype=int)

print(np.sum(arr, dtype=int)) # 390
print(np.sum(arr, axis=0, dtype=int)) # [359  10  10  11]
print(np.sum(arr, axis=1, dtype=int)) # [222  32 136]

print(np.prod(arr, dtype=int)) # 35142290640
print(np.prod(arr, axis=0, dtype=int)) # [602577     36     36     45]
print(np.prod(arr, axis=1, dtype=int)) # [5751  621 9840]

print(np.min(arr)) # 3
print(np.min(arr, axis=0)) # [23  3  3  3]
print(np.min(arr, axis=1)) # [3 3 4]

print(np.max(arr)) # 213
print(np.max(arr, axis=0)) # [213   4   4   5]
print(np.max(arr, axis=1)) # [213  23 123]

print(np.mean(arr))
print('%.2f' % np.std(arr))

print(np.median(arr))
print(np.median(arr, axis=0))
print(np.median(arr, axis=1)) 