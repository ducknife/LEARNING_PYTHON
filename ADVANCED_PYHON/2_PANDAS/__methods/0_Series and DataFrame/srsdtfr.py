import pandas as pd

S = pd.Series([1, 2, 4], index=['A', 'B', 'C'])
print(S)

df = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'John'],
    'age' : [20, 21, 22],
    'department' : ['HR', 'IT', 'MK'],
    'salary' : [2000, 4000, 3000]
})
# orient mặc định là columns.
print(df)

df2 = pd.DataFrame.from_dict({
    'name' : ['Hung', 'Mai', 'Tam'],
    'age' : [20, 20, 20]
}, orient='index', columns=['colA', 'colB', 'colC'])
# orient = 'index' thì key sẽ là row.
# orient = 'columns' thì key sẽ là columns.
# columns sẽ là các nhãn cho các cột.
print(df2)

# mỗi cột của DataFrame là 1 Series.