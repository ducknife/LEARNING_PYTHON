from collections import Counter

a = [1, 1, 2, 2, 4, 4, 5, 6, 67, 7, 87]
b = dict(Counter(a))
print(b)
c = list(dict(Counter(a)).items())
print(c)

C = Counter(a)
print(C[67])