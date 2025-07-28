import os
import random as rd

DAU_VAO = '''
Ma trận kề vô hướng cỡ n x n
'''
DAU_RA = '''
Bậc của các đỉnh trên 1 dòng, cách  nhau bởi dấu cách 
'''

class matrix:
    def __init__ (self, n):
        self.mtx = [[0] * n for x in range(n)]

path_in = os.path.join(os.path.dirname(__file__), 'input')
path_out = os.path.join(os.path.dirname(__file__), 'output')

os.makedirs(path_in, exist_ok=True)
os.makedirs(path_out, exist_ok=True)

if __name__ == '__main__':
    for i in range(20):
        # Input Processing:
        # rd.seed(10)
        n = rd.randint(1, 10)
        mt = matrix(n)
        for idx in range(n):
            mt.mtx[idx][idx] = 0
            for jdx in range(idx + 1, n):
                # rd.seed(12)
                mt.mtx[idx][jdx] = rd.choices([0, 1], weights=[10, 90], k=1)[0]
                mt.mtx[jdx][idx] = mt.mtx[idx][jdx]
        path_i = f'{path_in}/input{i}.inp'
        path_o = f'{path_out}/output{i}.out'
        with open(path_i, 'w', encoding='utf-8') as f:
            f.write(f'{n}\n')
            for idx in range(n):
                row_s = ' '.join(str(x) for x in mt.mtx[idx])
                f.write(f'{row_s}\n')
        # Output Processing:
        deg = [0 for i in range(n + 1)]
        for idx in range(n):
            for jdx in range(n):
                if mt.mtx[idx][jdx] == 1:
                    deg[idx + 1] += 1
                    deg[jdx + 1] += 1
        with open(path_o, 'w', encoding='utf-8') as f:
            for idx in range(1, n):
                f.write(f'{deg[idx] // 2} ')
            f.write(f'{deg[n] // 2}')