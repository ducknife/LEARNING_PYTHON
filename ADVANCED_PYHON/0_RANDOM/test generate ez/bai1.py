import random
import os
from solve import solve as sol

DAU_VAO = f'''
Dòng đầu tiên là số nguyên n (1 <= n <= 1000)
Dòng thứ hai là n số nguyên ai (-100 <= ai <= 100)
'''

list_n = [x for x in range(1, 1001)]

a = [x for x in range(-100, 101)]

path = os.path.join(os.path.dirname(__file__), 'input')

os.makedirs(path, exist_ok=True) 
#exist_ok = True, tạo thư mục chưa có, nếu có thì không làm gì, để False thì nếu có thư mục rồi sẽ lỗi
#makedirs : tạo thư mục cha dựa trên path nếu nó chưa có

path_out = os.path.join(os.path.dirname(__file__), 'output')
os.makedirs(path_out, exist_ok=True)

for i in range(10):
    n = random.choice(list_n)
    nums = random.choices(a, k=n)
    output = sol(nums)
    path_i = f'{path}/input{i}.inp'
    with open(path_i, 'w', encoding='utf-8') as f:
        f.write(f'{n} \n')
        f.write(' '.join(map(str,nums)))
    path_o = f'{path_out}/output{i}.out'
    with open(path_o, 'w', encoding='utf-8') as f:
        f.write(str(output))
