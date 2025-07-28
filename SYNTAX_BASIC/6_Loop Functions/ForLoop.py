#range(): range(start, stop, step) : from start to < stop

#default: start = 0, step = 1 neu khong co start va step

a = range(10)
for i in a:
    print(i, end = ' ')

print('\n')

for i in range(1, 51): #chay tu 1 -> 50
    print(i, end = ' ')
print('\n')

#for cung co else
for i in range(0, 51, 2): #chi in so chan khi step = 2
    print(i, end = ' ')
else:
    print('Vong for da ket thuc !')
