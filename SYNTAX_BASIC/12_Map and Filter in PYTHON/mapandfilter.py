
a = [-1, 2, -3, 4]
d = [21, 3, -1, 2]
b = list(map(abs, a))
print(b)

def add(a, b):
    return a + b

e = list(map(add, a, d))
print(e)


s = "dfasdf"
c = list(map(ord, s))
print(c)

g = [1, 3, 4, 1231]
h = list(filter(lambda x : x % 2 == 1, g))
print(h)