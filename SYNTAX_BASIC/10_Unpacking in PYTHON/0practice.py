data = ['Hung', 20, 'AI engineer']
name, age, job = data
print(name, age, job)

data = ((2, 3), (23, 343))
for x, y in data:
    print(x, y)

a = [1, 2, 3, 4]
x, y, *t = a
print(x, y, t)

b = {1, 2, 3}
s, n, _ = b
print(s, n)

a, b, c = range(0, 3)
print(a, b, c)

