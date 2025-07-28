import os
import random as rd
from solve import solve as sol

DAU_VAO = '''
Dòng đầu tiên là số n (1 <= n <= 100)
Tiêp theo là ma trận cỡ n x n với 0 <= a[i][j] <= 1000.
'''

class matrix:
    def __init__(self):
        self.mtrix = []

path_in = os.path.join(os.path.dirname(__file__), 'input')
path_out = os.path.join(os.path.dirname(__file__), 'output')

elements = [x for x in range(0, 2)]

os.makedirs(path_in, exist_ok=True)
os.makedirs(path_out, exist_ok=True)

if __name__ == '__main__':
    for i in range(20):
        n = rd.randint(1, 100)
        mt = matrix()
        for idx in range(n):
            row_idx = rd.choices(elements, k=n)
            mt.mtrix.append(row_idx)
        path_i = f'{path_in}/input{i}.inp'
        path_o = f'{path_out}/output{i}.out'
        with open(path_i, 'w', encoding='utf-8') as f:
            f.write(f'{str(n)}\n')
            for jdx in range(n):
                row_s = ' '.join(str(x) for x in mt.mtrix[jdx])
                f.write(f'{row_s}\n')
        output = sol(mt.mtrix)
        with open(path_o, 'w', encoding='utf-8') as f:
            f.write(f'{str(n)}\n')
            for jdx in range(n):
                row_s = ' '.join(str(x) for x in output[jdx])
                f.write(f'{row_s}\n')