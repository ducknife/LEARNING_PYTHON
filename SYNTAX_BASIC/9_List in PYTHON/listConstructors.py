#copy()

a = [1, 2, 3]
b = a.copy()
print(b)

#count(value) : tra ve so lan xuat hien cua value
print(a.count(1))

#index(value) : tra ve idx dau tien 
c = [1, 2, 1, 1, 1]
print(c.index(1))

#reverse()
d = [1, 2, 3, 4]
d.reverse()
print(d)

#sort()
e = [1, 2, 3, 4, 1]
e.sort()
print(e)

#min(), max(), sum(), sorted()

f = sorted(e)
print(f, e)