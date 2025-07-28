#range(start, end, step): default start = 0, step = 1
print("RANGE:")

a = range(10) #duyet tu 0 => 9

for i in a:
    print(i, end=' ')
print()

b = range(2, 10) #co start, khong co step

for i in b:
    print(i, end=' ')
print()


c = range(2, 10, 2) #co start, co step 

for i in c:
    print(i, end=' ')
print()

#for loop: else cua vong lap for la khi no ket thuc

print("FOR LOOP:")

for i in range(0, 10, 2):
    print(i, end=' ')
else:
    print('Vong lap da ket thuc') 

#while loop: else cua vong lap while cung khi no ket thuc

print("WHILE LOOP:")

d = 10

while d > 0:
    print(d, end=' ')
    d -= 1
else:
    print('Vong lap da ket thuc')