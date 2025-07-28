#Kiem tra hai doi tuong co phai la mot hay khong
#is
#is not
a, b = 100, 100
print(id(a))
print(id(b))
if (a is b):
    print('YES')
else:
    print('NO')
    
if (a is not b):
    print('yes')
else:
    print('no')