a = [1, 2, 3, 4, 5, 5]
print(len(a))

s = 'hung sinh ngay 12 thang 6 nam 2005'
print(list(s))


""" 1. them phan tu """
print("THEM PHAN TU VAO CUOI LIST BANG APPEND(VALUE)")
a.append('12')

print("THEM PHAN TU VAO VI TRI BAT KI BANG INSERT(INDEX, VALUE)")
a.insert(len(a), '06')
print(a)


""" 2. xoa phan tu """
print("DUNG POP() XOA PHAN TU TRONG LIST")
a.pop()
print(a)

print("DUNG POP(INDEX) XOA PHAN TU TRONG LIST")
a.pop(0)
print(a)

print("DUNG REMOVE XOA PHAN TU TRONG LIST")
a.remove(a[len(a) - 1])
print(a)

print("DUNG DEL list[index] XOA PHAN TU TRONG MANG")
del a[3]
print(a)

print("XOA MOI PHAN TU CUA LIST BANG CLEAR")
a.clear()
print(a)


""" 3. copy list """
print("COPY LIST")
c = [1, 2, 3, 4, 'hung']

d = c.copy()
e = c[:]
f = c #f se co cung id voi c
t = c * 2
print(t)

print(d, e, f, sep='\n')
print(id(d), id(e), id(f), id(c))

print("KHOI TAO MANG VOI N PHAN TU")
g = [True] * 100
print(g)

""" 4. tim kiem O(N) bang toan tu in"""
h = ['apple', 'samsung', 'oppo', 'xiaomi']

if 'apple' in h:
    print("YES")
else:
    print("NO")

""" 5. noi 2 list """

i = [1, 2, 45, 5]
j = [1, 2, 3, 4]
k = i + j
i.extend(j)

print(k, i, sep='\n')


""" 6. list constructor """

l = [1, 12, 1212, 1212, 23]

l.sort()
print(l)

l.reverse()
print(l)

print(l.count(1212))
print(l.index(12))

m = [121, 323, 23, 233]
n = sorted(m)
print(m, n, sep='\n')

""" 7. list slicing """
o = [1, 2, 3, 4, 5]
p = o[:5]
print(p)

q = o[::-1]
print(q)

o[:0] = [0, 0, 0]
print(o)

o[len(o):] = [0, 0, 0]
print(o)

o[1:2] = [1]
print(o)

""" 8. list comprehension """

a = [12, 21, 30]
b = [x * 2 for x in a] 
print(b) #2, 4, 6

def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

c = [sumDigits(x) for x in a]
print(c) #3, 3, 3

d = [x for x in a if x > 20]
print(d) #21, 30

e = list(map(lambda x : x ** 2, a))
print(e) #144, 441, 900
