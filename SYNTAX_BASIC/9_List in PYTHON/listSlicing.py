""" list slicing: [start : stop : step] : cắt từ start đến stop - 1, step mặc định là 1, start mặc định là 0, stop mặc định là cắt
đến phần tử cuối cùng"""

a = [1, 2, 3, 4, 5, 6]

b = a[1:5:1] 
print(b)
print()

""" lật ngược list bằng list slicing """
print(a[::-1])
print(a)
print()

""" thay đổi phần tử """
c = [1, 2, 3, 4]
c[0:2] = [10, 100]
print(c)

""" chèn phần tử """

d = [1, 33, 21, 21, 23]
d[:0] = [10, 200, 200] #chèn vào đầu list
print(d)

d[len(d):] = [0, 0, 0] #chèn phần tử vào cuối
print(d)

""" copy list """
e = [1, 2, 3]
f = e[:]
print(f)