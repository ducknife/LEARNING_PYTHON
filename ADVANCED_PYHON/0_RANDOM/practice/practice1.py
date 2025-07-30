from datetime import datetime as dtime
import os
import random as rd

DAUVAO = '''Tạo 50 file .txt chứa ma trận n x m chiều
trong đó có 10 file ma trận toàn số 0, 10 file ma trận toàn số 1, 20 file ma trận đơn vị,
10 file là ma trận có giá trị trong [0, 100]'''

now = dtime.now().strftime("File is running at %d/%m/%Y %H:%M:%S")
print(now)

nms = [x for x in range(1, 101)]

path = os.path.join(os.path.dirname(__file__), 'MATRIX INPUT')
os.makedirs(path, exist_ok=True)

def write_file(n, m, pathi, matrix):
    with open(pathi, 'w', encoding='utf-8') as f:
        f.write(f'{n} {m if m else ''}\n')
        for i in range(n):
            f.write(' '.join(map(str, matrix[i])))
            f.write('\n')

def getN():
    n = rd.randint(1, 101)
    return n

def getNM():
    nm = rd.sample(nms, k=2)
    return nm

if __name__ == '__main__':
    for _ in range(50):
        if _ < 10:
            n, m = getNM()
            pathi = f'{path}/ZEROS{_}.txt'
            ZEROS = [[0 for i in range(m)] for i in range(n)]
            write_file(n, m, pathi, ZEROS)
        elif _ < 20:
            n, m = getNM()
            pathi = f'{path}/ONES{_}.txt'
            ONES = [[1 for i in range(m)] for i in range(n)]
            write_file(n, m, pathi, ONES)
        elif _ < 40:
            n = getN()
            pathi = f'{path}/IDENTITY{_}.txt'
            IDENTITY = [[0 for i in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        IDENTITY[i][j] = 1
            write_file(n, 0, pathi, IDENTITY)
        else:
            n, m = getNM()
            pathi = f'{path}/NORMAL{_}.txt'
            NORMAL = []
            for i in range(n):
                rowi = rd.choices([x for x in range(101)], k=m)
                NORMAL.append(rowi)
            write_file(n, m, pathi, NORMAL)