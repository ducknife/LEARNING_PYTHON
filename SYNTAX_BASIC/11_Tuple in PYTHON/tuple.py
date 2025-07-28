""" tuple không thể thay đổi, nhưng phần tử trong nó mà thay đổi được thì phần tử đó vẫn thay đổi được"""
init_tuple = tuple()

a = (1, 2, 3)
b = ("a", "a", 1)
print(a, b)
c = (a, b, '1')
print(c)

for i in a:
    print(i)

""" sắp xếp tuple """

d = (3, 12, 1)
d = tuple(sorted(d))
print(d)

""" tuple constructor """
print(d.count(3))
print(d.index(12))
