import pandas as pd

data = {
    'username' : ['hungdeptrai', 'hungvippro', 'hungestimate'],
    'password' : ['nguoideptrai', 'nguoivippro', 'nguoiestimate']
}

df = pd.DataFrame(data, index=['A', 'B', 'C'])

print(df.head(1)) # in ra 1 dòng đầu.
print(df.tail(1)) # in ra 1 dòng cuối 
print(df.info()) # hiển thị kiểu dữ liệu và thông tin cột.
print(df.describe()) # thống kê mô tả.

# properties
print(df.shape) # trả về 1 tuple.
print(df.columns) # in ra thông tin cột.
print(df.dtypes) # in ra kiểu dữ liệu.