import numpy as np
import os

a = np.array([1, 2, 3, 4], dtype=int)
b = np.array([[123, 23], [123, 23]], dtype=int)
print(a, b, sep='\n')

c = np.zeros((2, 3), dtype=int)
d = np.ones((2, 3), dtype=int)
print(c, d, sep='\n')

e = np.eye(3, 4, k=0, dtype=int) # trong đường chéo chính, với rect, thì chính bắt đầu từ array[0][0]
e1 = np.eye(3, 4, k=1, dtype=int) # trên đường chéo chính
e2 = np.eye(3, 4, k=-1, dtype=int) # dưới đường chéo chính
f = np.identity(3, dtype=int)
f1 = np.full((2, 3), 6, dtype=int) # mảng toàn số 6
f2 = np.linspace(2, 10, 5, endpoint=True, retstep=True, dtype=int) # các điểm đều nhau
print(e, e1, e2, f, f1, f2, sep='\n')

g = np.random.rand(2, 3) # trong đoạn [0, 1)
g1 = np.random.randn(2, 3) # theo phân phối chuẩn.
g2 = np.random.randint(2, 4, 10) # trong đoạn [2, 4), với 10 phần tử. 
print(g, g1, g2, sep='\n')

DAU_VAO = 'Dòng đầu gồm một số nguyên n' \
'tiếp theo là n số nguyên dương với 0 <= a[i] <= 1000'

path = os.path.join(os.path.dirname(__file__), 'input')
os.makedirs(path, exist_ok=True)

def make_input():
    for i in range(50):
        n = np.random.randint(1, 101, 1)[0]
        arr = np.random.randint(0, 1001, n)
        path_in = f'{path}/input{i}.txt'
        with open(path_in, 'w', encoding='utf-8') as f:
            f.write(f'{n}\n')
            f.write(' '.join(map(str, arr)))

make_input()