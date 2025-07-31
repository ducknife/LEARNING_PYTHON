import numpy as np

a = np.array([12, 3, 4, 5], dtype=int)

# sum and product
print(np.sum(a, dtype=int))
print(np.prod(a, dtype=int))

b = np.array([[12, 3, 4], [12, 4, 5]], dtype=int)
print(np.sum(b, dtype=int)) # tính toàn bộ
print(np.sum(b, axis=0, dtype=int)) # tổng từng cột . output: [24 7 9]
print(np.sum(b, axis=1, dtype=int)) # tổng từng hàng . ouput: [19 21]

# tính kỳ vọng (trung bình) và độ lệch chuẩn
print(np.mean(a, dtype=int))
print('{:.2f}'.format(np.std(a)))

# tính min, max
print(np.min(a)) # tìm min toàn bộ array
print(np.min(b, axis=0)) # tìm min từng cột . output : [12 3 4]
print(np.min(b, axis=1)) # tìm min từng hàng . output: [3 4]

print(np.max(a)) # output: 12
print(np.max(b, axis=0)) # output: [12 4 5]
print(np.max(b, axis=1)) # output: [12 12]

# tính median: trung bình cộng hai phần tử ở giữa nếu n chẵn, ngược lại thì là phần tử giữa sau khi sắp xếp tăng 
print(np.median(a)) # 4.5
print(np.median(b, axis=0)) # tính median từng cột . output: [12. 3.5 4.5]
print(np.median(b, axis=1)) # tính median từng hàng . output: [4. 5.]
