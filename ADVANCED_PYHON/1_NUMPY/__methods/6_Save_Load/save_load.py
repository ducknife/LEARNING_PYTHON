import numpy as np
import os

arr = np.array([1, 3, 4, 5], dtype=int) # lưu vào file .npy 
np.save('array.npy', arr)

arr = np.load('array.npy') # load data
print(arr)

path = os.path.join(os.path.dirname(__file__), 'load_save')

np.save(path, arr)

path2 = os.path.join(os.path.dirname(__file__), 'input')
os.makedirs(path2, exist_ok=True)

np.save(f'{path2}/save', arr)

arr2 = np.load(f'{path2}/save.npy')
print(arr2)