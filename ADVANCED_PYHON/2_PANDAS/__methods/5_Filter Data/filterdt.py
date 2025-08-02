import pandas as pd

data = {
    'salary' : [2000, 3000, 4000, 1000, 2500]
}

df = pd.DataFrame(data)

A = df[df > 2000]

print(A.dropna(axis=0))

B = df[(df > 2000) & (df < 4000)]

print(B.dropna(axis=0))

print(A.fillna(126))
