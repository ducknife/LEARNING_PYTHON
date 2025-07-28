a = [1, 2, 4, 5, 5]
b = list(map(lambda x : x ** 2, a))
c = list(filter(lambda x : x % 2 == 1, a))
print(b, c)