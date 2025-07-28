



""" lambda parameters : expression """

sum = lambda x, y, z : x + y + z

print(sum(10, 20, 209))
print(sum(y = 1, z = 10, x = 11))

""" lambda với map() """
a = [1, 2, 3]
b = list(map(lambda x : x**2, a)) #tao ra mang gom cac phan tu la binh phuong
print(b)

""" lambda với filter """
c = list(filter(lambda x : x % 2 == 1, a)) #loc cac phan tu la so le trong a vao b
print(c)

""" lambda với if else """
FIND_MAX = lambda x, y : x if x > y else y
print(FIND_MAX(2, 4))
