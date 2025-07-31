import numpy as np

cs = np.array(['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'], dtype=str)

b = np.unique(cs, return_counts=True)

print(b[0], b[1])