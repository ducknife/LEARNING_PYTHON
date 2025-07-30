from datetime import datetime as dtime
import os
import numpy as np

DAUVAO = '''Tạo 50 file .txt chứa ma trận n x m chiều
trong đó có 10 file ma trận toàn số 0, 10 file ma trận toàn số 1, 20 file ma trận đơn vị,
10 file là ma trận có giá trị trong [0, 100]'''

now = dtime.now().strftime("File is running at %d/%m/%Y, %H:%M:%S")
print(now)

PATH = os.path.join(os.path.dirname(__file__), 'MATRIX INPUT')
os.makedirs(PATH, exist_ok=True)

def get_NM():
    a = np.random.randint(1, 101, 2, dtype=int)
    return a

def get_N():
    n = np.random.randint(1, 101, 2, dtype=int)[0]
    return n

def write_file(n, m, pathi, matrix):
    with open(pathi, 'w', encoding='utf-8') as f:
        f.write(f'{n} {m if m > 0 else ''}\n')
        for i in range(n):
            f.write(' '.join(map(str, matrix[i])))
            f.write('\n')

if __name__ == '__main__':
    for _ in range(50):
        if _ < 10:
            pathi = f'{PATH}/ZEROS{_}.txt'
            n, m = get_NM()
            ZEROS = np.zeros((n, m), dtype=int)
            write_file(n, m, pathi, ZEROS)
        elif _ < 20:
            pathi = f'{PATH}/ONES{_}.txt'
            n, m = get_NM()
            ONES = np.ones((n, m), dtype=int)
            write_file(n, m, pathi, ONES)
        elif _ < 40:
            pathi = f'{PATH}/IDENTITY{_}.txt'
            n = get_N()
            IDENTITY = np.eye(n, dtype=int)
            write_file(n, 0, pathi, IDENTITY)
        else:
            pathi = f'{PATH}/NORMAL{_}.txt'
            n, m = get_NM()
            mt_tmp = []
            for i in range(n):
                mt_tmp.append(np.random.randint(0, 101, m, dtype=int))
            MATRIX = np.array(mt_tmp, dtype=int)
            write_file(n, m, pathi, MATRIX)
