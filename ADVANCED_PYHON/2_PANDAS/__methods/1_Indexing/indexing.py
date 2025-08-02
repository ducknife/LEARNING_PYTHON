import pandas as pd

users = {
    'name' : ['Hung', 'Van', 'Mai'],
    'email' : ['hungnv@gmail.com', 'vantt@gmail.com', 'mailnt@gmail.com']
}

df = pd.DataFrame(users, index=['a', 'b', 'c'])
print(df)

print(df['name']) # 1 series.

print(df.loc['a', 'email']) # truy cập theo nhãn.
print(df.iloc[1, 0]) # truy cập theo chỉ số. Hàng 1, cột 0

