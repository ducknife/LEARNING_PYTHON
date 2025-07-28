import numpy as np
import pandas as pd

# ============================
# NumPy: Numerical Computing
# ============================

# 1. Creating Arrays
array_1d = np.array([1, 2, 3])  # 1D array
array_2d = np.array([[1, 2], [3, 4]])  # 2D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # 3D array

# 2. Array Properties
print(array_2d.shape)  # Shape of array
print(array_2d.ndim)   # Number of dimensions
print(array_2d.size)   # Total number of elements
print(array_2d.dtype)  # Data type of elements

# 3. Array Operations
array_sum = array_1d + 10  # Add scalar
array_product = array_1d * 2  # Multiply scalar
array_add = array_1d + np.array([4, 5, 6])  # Element-wise addition
array_dot = np.dot(array_1d, array_1d)  # Dot product

# 4. Useful Functions
zeros = np.zeros((3, 3))  # Array of zeros
ones = np.ones((2, 2))  # Array of ones
identity = np.eye(3)  # Identity matrix
random = np.random.rand(3, 3)  # Random values

# 5. Indexing and Slicing
print(array_2d[0, 1])  # Access element
print(array_2d[:, 0])  # Access column
print(array_2d[0, :])  # Access row

# 6. Mathematical Functions
array_sqrt = np.sqrt(array_1d)  # Square root
array_exp = np.exp(array_1d)  # Exponential
array_mean = np.mean(array_1d)  # Mean
array_std = np.std(array_1d)  # Standard deviation

# 7. Reshaping and Transposing
reshaped = array_1d.reshape((3, 1))  # Reshape array
transposed = array_2d.T  # Transpose array

# ============================
# pandas: Data Manipulation
# ============================

# 1. Series
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # Create Series
print(series['a'])  # Access element by index
print(series.mean())  # Compute mean

# 2. DataFrame Creation
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)  # Create DataFrame

# 3. Accessing Data
print(df['Name'])  # Access column
print(df.iloc[0])  # Access row by position
print(df.loc[0, 'Name'])  # Access specific cell

# 4. Modifying Data
df['Age'] = df['Age'] + 1  # Modify column
df['Salary'] = [50000, 60000]  # Add new column

# 5. DataFrame Operations
print(df.describe())  # Summary statistics
print(df.sort_values('Age'))  # Sort by column
print(df.drop('Salary', axis=1))  # Drop column

# 6. Handling Missing Data
df_missing = pd.DataFrame({'A': [1, np.nan], 'B': [np.nan, 2]})
print(df_missing.fillna(0))  # Fill missing values
print(df_missing.dropna())  # Drop rows with missing values

# 7. Grouping and Aggregation
grouped = df.groupby('Age').mean()  # Group by column and compute mean

# 8. Reading/Writing Data
df.to_csv('output.csv', index=False)  # Write to CSV
df_read = pd.read_csv('output.csv')  # Read from CSV

# ============================
# Advanced Topics
# ============================

# NumPy Broadcasting
array_broadcast = array_2d + np.array([1, 2])  # Add row-wise

# pandas Merging and Joining
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2], 'Salary': [50000, 60000]})
merged = pd.merge(df1, df2, on='ID')  # Merge DataFrames

# pandas Pivot Tables
pivot = df.pivot_table(values='Salary', index='Age', aggfunc='mean')

# pandas Time Series
date_range = pd.date_range(start='2025-01-01', end='2025-01-10')
time_series = pd.Series(range(10), index=date_range)

# Explore the documentation for more advanced features!