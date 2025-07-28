a, b = 0, 1
print(a, b, sep = '\n')
i = 2
while i <= 100:
    x = a + b
    print(x)
    a, b = b, x
    i += 1
