import numpy as np

cs = np.array(['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'], dtype='S')

print(cs.dtype)
b = np.unique(cs, return_counts=True)

print(b[0], b[1])