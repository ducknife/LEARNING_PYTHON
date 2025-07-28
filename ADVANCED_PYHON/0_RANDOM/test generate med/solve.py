import os
from functools import cmp_to_key

def cmp(a, b):
    if a.salary != b.salary:
        return -1 if a.salary > b.salary else 1
    if a.name != b.name:
        return -1 if a.name < b.name else 1
    return 0

def solve(clients):
    clients.sort(key=cmp_to_key(cmp))
    return clients