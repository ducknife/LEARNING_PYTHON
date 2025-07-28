# input() tra ve xau ki tu, doc ca mot dong
s = input('Nhap xau s vao day : ')
print(s)
integer = int(input('Nhap so nguyen n: '))
float = float(input('Nhap so thuc f: '))
print(integer, float, end = '!\n')
print(integer**2)

# cach nhap nhieu so tu mot dong
d = input()

#a la list cac xau trong duoc tach ra trong d
a = d.split()

#chuyen ve cac so bang map(kieu du lieu, a)
x, y, z = map(int, a)
print(x, y, z)
x, y, z = map(int, input().split())
print(x, y, z)
e = input();
c = e.split() 
g, h, k = map(int, c)
print(g, h, k)
p, q, r = map(int, input().split())
print(p, q, r)

""" split : phan re/ phan chia """