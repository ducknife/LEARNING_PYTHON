import random
from collections import Counter

ho = ["Nguyễn", "Trần", "Lê", "Vũ", "Phạm", "Đỗ", "Mai", "Chu"]
dem = ["Văn", "Thị", "Ngọc", "Lê Ngọc", "Diễm", "Minh"]
ten = ["Hùng", "Quỳnh", "Mai", "Vân", "Ngân", "Yến", "Hiền"]

def make_random_name():
    return f'{random.choice(ho)} {random.choice(dem)} {random.choice(ten)}'


user_list = []

for _ in range(100):
    user_list.append(make_random_name())

C = Counter(user_list)
dic = dict(C.items())
for key, val in dic.items():
    print(key, ":", val, "lần")