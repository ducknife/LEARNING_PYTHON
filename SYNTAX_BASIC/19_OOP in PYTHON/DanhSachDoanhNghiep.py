import os
from functools import cmp_to_key

class DoanhNghiep:
    def __init__ (self, id, name, num):
        self.id = delete_ws(id)
        self.name = delete_ws(name)
        self.num = num
    def __str__(self):
        return f'{self.id} {self.name} {self.num}'
    
def delete_ws(name):
    tmp = name.strip().split()
    res = ' '.join(tmp)
    return res

def cmp(a, b):
    if a.num != b.num:
        return -1 if a.num > b.num else 1
    if a.id != b.id:
        return -1 if a.id < b.id else 1
    return 0

if __name__ == '__main__':
    n = int(input())
    dn_list = []
    for _ in range(n):
        id = input()
        name = input()
        num = int(input())
        dn = DoanhNghiep(id, name, num)
        dn_list.append(dn)
    dn_list.sort(key=cmp_to_key(cmp))
    for x in dn_list:
        print(x)
