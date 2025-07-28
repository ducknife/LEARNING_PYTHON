import random
from solve import solve as sol
import os

DAU_VAO = '''
Dòng đầu là số nguyên n (1 <= n <= 200),
tiếp theo là n khách hàng,
mỗi khách hàng có các thông tin nhập theo thứ tự:
- Tên
- Ngày sinh
- Vị trí
- Lương
'''

class client:
    def __init__ (self, name, bod, pos, sal):
        self.name = name
        self.birth_of_date = bod
        self.position = pos
        self.salary = sal
    def on_screen(self):
        return f'{self.name}\n{self.birth_of_date}\n{self.position}\n{self.salary}\n'

valid_month = [month for month in range(1, 13)]

valid_year = [year for year in range(1990, 2005)]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]

first_names = [
    "James", "John", "Robert", "Michael", "William",
    "David", "Richard", "Joseph", "Thomas", "Charles",
    "Christopher", "Daniel", "Matthew", "Anthony", "Mark",
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth",
    "Barbara", "Susan", "Jessica", "Sarah", "Karen",
    "Nancy", "Lisa", "Betty", "Margaret", "Sandra"
]

positions = [
    "CEO",
    "COO",
    "CFO",
    "CTO",
    "VP",
    "Dir.",
    "Sr. Mgr",
    "Mgr",
    "TL",
    "Sr. Spec",
    "Spec",
    "Staff",
    "Intern"
]

path_in = os.path.join(os.path.dirname(__file__), 'input')
path_out = os.path.join(os.path.dirname(__file__), 'output')

os.makedirs(path_in, exist_ok=True)
os.makedirs(path_out, exist_ok=True)

def make_date(client_y, client_m, client_d):
    is_setdate = False
    if client_y % 4 == 0 and client_y % 100 or client_y % 400 == 0:
        if client_m == 2:
            client_d = random.randint(1, 29)
            is_setdate = True
    else:
        if client_m == 2:
            client_d = random.randint(1, 28)
            is_setdate = True
    if not is_setdate:
        if client_m in {1, 3, 5, 7, 8, 10, 12}:
            client_d = random.randint(1, 31)
        else:
            client_d = random.randint(1, 30)
    return f'{'0' if client_d < 10 else ''}{client_d}/{'0' if client_m < 10 else ''}{client_m}/{client_y}'

def make_name(client_fname, client_lname):
    return f'{client_fname} {client_lname}'

if __name__ == '__main__':
    for i in range(50):
        n = random.randint(1, 200)
        clients = []
        for _ in range(n):
            client_fname = random.choice(first_names)
            client_lname = random.choice(last_names)
            client_y = random.choice(valid_year)
            client_m = random.choice(valid_month)
            client_d = None
            client_bod = make_date(client_y, client_m, client_d)
            client_salary = random.randint(10000000, 100000000)
            client_position = random.choice(positions)
            new_client =  client(make_name(client_fname, client_lname), client_bod, client_position, client_salary)
            clients.append(new_client)
        path_i = f'{path_in}/input{i}.txt'
        path_o = f'{path_out}/output{i}.txt'
        with open(path_i, 'w', encoding='utf-8') as f:
            f.write(f'{n}\n')
            for c in clients:
                f.write(c.on_screen())
        output = sol(clients)
        with open(path_o, 'w', encoding='utf-8') as f:
            f.write(f'{n}\n')
            for c in output:
                f.write(c.on_screen())