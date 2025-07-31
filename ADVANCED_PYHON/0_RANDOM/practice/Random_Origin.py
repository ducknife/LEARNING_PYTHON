import random
from collections import Counter
import os 

ho = ["Nguyễn", "Trần", "Lê", "Vũ", "Phạm", "Đỗ", "Mai", "Chu"]
dem = ["Văn", "Thị", "Ngọc", "Lê Ngọc", "Diễm", "Minh"]
ten = ["Hùng", "Quỳnh", "Mai", "Vân", "Ngân", "Yến", "Hiền"]

def make_random_name():
    return f'{random.choice(ho)} {random.choice(dem)} {random.choice(ten)}'


user_list = []

for _ in range(1000):
    user_list.append(make_random_name())

PATH = os.path.join(os.path.dirname(__file__), 'result.txt')


C = Counter(user_list)
dic = dict(C.items())

with open(PATH, 'w', encoding='utf-8') as f:
    for key, val in dic.items():
        f.write(f'Tên: {key} xuất hiện {val} lần\n')