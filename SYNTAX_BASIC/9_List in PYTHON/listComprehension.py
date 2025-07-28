""" syntax: [expression for var in iterable] """

a = [1, 2, 3]
b = [x * 2 for x in a]
print(b)

c = [1, 2, 3, 4]
d = [x ** x for x in c]
print(d)

e = [x * 2 for x in range(0, 10)]
print(e)


""" [function for var in iterablez] """
def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

f = [2, 323, 21131212, 12]
g = [sumDigits(x) for x in f]
print(g)

""" [expression for var in iterable if <clause>] """

h = [1, 2, 3]
i = [x for x in h if x % 2 == 1] 
print(i)

j = list(map(lambda x : x ** 2, h))
print(j)

k = list(filter(lambda x : x % 2 == 1, a))
print(k)