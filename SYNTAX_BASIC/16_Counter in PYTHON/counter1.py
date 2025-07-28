from collections import Counter
#thu tu xuat hien trong counter la thu tu xuat hien ban dau
a = [1, 2, 3, 4]
b = Counter(a)
d = dict(Counter(a))
print(b)
print(type(b))
print(d)
print(type(d))
l = list(dict(Counter(a)).items())
print(l)
print(type(l))