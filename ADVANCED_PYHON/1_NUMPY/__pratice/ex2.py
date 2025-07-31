import numpy as np

sales_data = np.array([120, 100, 150, 130, 170, 110, 140], dtype=int)

max_day = np.argmax(sales_data)
min_day = np.argmin(sales_data)

print(max_day, min_day)