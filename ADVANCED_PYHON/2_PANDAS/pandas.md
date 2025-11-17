# Introduction to Pandas

**Pandas** is a powerful and open-source Python library for data manipulation and analysis. It provides high-performance, easy-to-use data structures and data analysis tools that make it a cornerstone of data science and machine learning workflows. Built on top of NumPy, pandas excels at handling structured (tabular) data, such as data from spreadsheets, SQL tables, or CSV files.

### Why Use Pandas?
- **Intuitive Data Structures:** Simplifies working with labeled and relational data.
- **High Performance:** Optimized for speed, even with large datasets.
- **Flexible Data Handling:** Easily reads and writes data from various formats (CSV, Excel, SQL, JSON).
- **Powerful Toolset:** Offers a rich set of functions for cleaning, transforming, merging, and reshaping data.
- **Strong Integration:** Works seamlessly with other data science libraries like NumPy, Matplotlib, and Scikit-learn.

---

## Core Data Structures

Pandas introduces two primary data structures: the `Series` and the `DataFrame`.

### 1. Series
A **Series** is a one-dimensional labeled array, similar to a column in a table. It can hold any data type (integers, strings, floating-point numbers, Python objects, etc.).

```python
import pandas as pd
import numpy as np

# Creating a Series from a list
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
```

### 2. DataFrame
A **DataFrame** is a two-dimensional labeled data structure with columns of potentially different types, much like a spreadsheet or a SQL table. It is the most commonly used pandas object.

```python
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)
print(df)
```

---

## The Most Useful Pandas Syntax

Here is a collection of the most common and useful pandas operations.

### Reading and Writing Data
Pandas makes it incredibly simple to read from and write to various file formats.

```python
# Read from a CSV file
df_csv = pd.read_csv('my_data.csv')

# Write to a CSV file
df.to_csv('output.csv', index=False) # index=False prevents writing row indices

# Read from an Excel file
df_excel = pd.read_excel('my_data.xlsx', sheet_name='Sheet1')

# Write to an Excel file
df.to_excel('output.xlsx', sheet_name='SalesData')
```

### Inspecting Your Data
Quickly get an overview of your DataFrame.

```python
# View the first 5 rows
print(df.head())

# View the last 5 rows
print(df.tail())

# Get a concise summary of the DataFrame
print(df.info())

# Get descriptive statistics for numerical columns
print(df.describe())

# Get the dimensions (rows, columns) of the DataFrame
print(df.shape)

# List the column names
print(df.columns)
```

### Selecting Data
Pandas offers multiple ways to select and filter data.

```python
# Select a single column (returns a Series)
ages = df['Age']

# Select multiple columns (returns a DataFrame)
subset = df[['Name', 'City']]

# Select rows by integer position using .iloc
first_row = df.iloc[0]
first_three_rows = df.iloc[0:3]

# Select rows by label (index) using .loc
# If the index is default integers, it behaves like .iloc
row_one = df.loc[0]

# Conditional filtering (Boolean indexing)
people_over_30 = df[df['Age'] > 30]
chicago_residents = df[df['City'] == 'Chicago']
```

### Data Manipulation
Modify your DataFrame by adding, removing, or renaming columns.

```python
# Add a new column
df['Salary'] = [70000, 80000, 90000, 100000]

# Create a new column based on existing ones
df['Age_in_5_Years'] = df['Age'] + 5

# Remove a column
df = df.drop('Salary', axis=1) # axis=1 specifies column

# Rename columns
df = df.rename(columns={'Name': 'Full Name', 'City': 'Location'})
```

### Handling Missing Data
Data cleaning often involves dealing with missing values (represented as `NaN`).

```python
# Create a sample DataFrame with missing values
data_with_nan = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]}
df_nan = pd.DataFrame(data_with_nan)

# Check for missing values
print(df_nan.isnull().sum())

# Drop rows with any missing values
df_cleaned = df_nan.dropna()

# Fill missing values with a specific value (e.g., 0 or the mean)
df_filled = df_nan.fillna(0)
mean_b = df_nan['B'].mean()
df_filled_mean = df_nan.fillna({'B': mean_b})
```

### Grouping and Aggregating
The `groupby` operation is one of the most powerful features of pandas. It allows you to split data into groups, apply a function to each group, and combine the results.

```python
# Group by a column and calculate the mean of other columns
age_by_city = df.groupby('Location')['Age'].mean()
print(age_by_city)

# Group by multiple columns and perform multiple aggregations
stats = df.groupby('Location')['Age'].agg(['mean', 'max', 'count'])
print(stats)
```

### Merging and Joining DataFrames
Combine multiple DataFrames using database-style join operations.

```python
# Create two sample DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]})

# Merge (like an SQL join)
merged_df = pd.merge(df1, df2, on='key', how='inner') # inner, outer, left, right
print(merged_df)

# Concatenate (stack DataFrames)
concatenated_df = pd.concat([df1, df2])
print(concatenated_df)
```

### Applying Functions
Apply a function along an axis of a DataFrame or to its elements.

```python
# Apply a function to each element in a column
df['Age_Squared'] = df['Age'].apply(lambda x: x**2)

# Apply a function to the entire DataFrame
numeric_df = df[['Age', 'Age_Squared']]
df_log = numeric_df.apply(np.log)
print(df_log)
```
