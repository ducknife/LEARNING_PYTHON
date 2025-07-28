""" set trong python khong co thu tu, tu loai bo phan tu trung nhau, khong the luu phan tu thay doi duoc """

# set init
init_set = set()

s = {11, 3, 3, 23, 4, 2}
print(s)

t = {(1, 2, 3), (123, 213)}
print(t)

""" set constructor """
a = [1, 3, 3, 3, 1]
a = set(a)
print(a)
a = list(a)
print(a)

""" them phan tu vao set """
s.add(121)
s.add(3) #3 da co thi set khong cho vao
print(s)

""" xoa phan tu khoi set """
s.discard(1233)
s.pop() #xoa ngau nhien
print(s)
s.remove(11)
print(s)
s.clear()

""" tim kiem trong set : o(1) """

d = [1, 23, 3]
if 1 in d:
    print("YES")
else:
    print("NO")

    

