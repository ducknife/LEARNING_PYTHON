import pandas as pd

data = {
    'name' : ['hihi', 'haha', 'hoho'],
    'age' : [20, 21, None]
}

df = pd.DataFrame(data)

print(df.isnull()) # True nếu là NaN.
print(df.notnull()) # False nếu là NaN.

print(df.fillna(10)) # Thay NaN thành 10.
print(df.dropna(axis=1)) # duyệt cột của hàng.
print(df.dropna(axis=0)) # duyệt hàng của cột.

