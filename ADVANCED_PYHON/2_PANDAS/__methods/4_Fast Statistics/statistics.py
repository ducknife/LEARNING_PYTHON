import pandas as pd

data = {
    'name' : ['Hung', 'Van', 'Mai'],
    'age' : [20, 18, 20]
}

df = pd.DataFrame(data)

print(df['age'].mean())
print(df['age'].std())
print(df['age'].value_counts()) # trả về số lần xuất hiện.
print(df['age'].value_counts(normalize=True)) # normalize=True : trả về tỉ lệ.

