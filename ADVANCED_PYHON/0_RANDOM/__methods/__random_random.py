import random

x = random.random() #sinh 1 số thực ngẫu nhiên trong [0.0, 1.0)

print('%.2f' % x)

y = random.uniform(10, 100) #sinh 1 số thực trong [a, b]

print('{:.2f}'.format(y))

z = random.randint(10, 100) #sinh 1 số nguyên trong [a, b]

print(z)

t = random.randrange(0, 10, 2) #sinh 1 số nguyên trong range

print(t) 