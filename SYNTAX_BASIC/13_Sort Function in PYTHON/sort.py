""" TIM SORT : mergesort and insertion sort """

a = [2, 123, 121312, 41234]
a.sort()
print(a)

b = [123, 3, 4, 121]
b.sort(reverse=True)
print(b)

""" tieu chi sap xep:: cung tieu chi thi khong doi vi tri """
c = [-1, 2, -110, 203]
c.sort(key= lambda x : abs(x))
print(c)

d = [12, 33, 10, 22]
def sumdigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

d.sort(key=sumdigit)
print(d)

""" sort trong nested list """
p = [[1, 2], [2, 1], [2, 2]]
p.sort(key=lambda x : (x[0], -x[1])) #sap xep theo phan tu dau tang dan, phan tu sau giam dan
print(p)

q = [2493, 2343123, 2349]
q.sort(key=lambda x : -x)
print(q)