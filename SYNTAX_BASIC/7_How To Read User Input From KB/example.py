#Nhập xâu, số từ bàn phím

d = input()
print(d)

f = int(input())
print(f)

g = float(input())
print(g)




#Nhập nhiều số từ bàn phím

s = input() #'12 23 3'
a = s.split() #a la mot list
print(a)
x, y, z = map(int, s.split()) 
print(x, y, z, sep=' ')


print("nhap ba so a, b, c: ")
a, b, c = map(int, input().split())

print(a, b, c, sep=', ')

