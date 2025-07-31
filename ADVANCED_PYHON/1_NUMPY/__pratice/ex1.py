import numpy as np

tempsX = np.array([25, 28, 30, 27, 29, 31, 26])

""" z-score = (X- E) / ơ """

E = np.mean(tempsX)
o = np.std(tempsX)

z_score = (tempsX - E) / o

print(z_score)
