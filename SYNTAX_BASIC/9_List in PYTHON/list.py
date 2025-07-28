# init a list: mot list co the chua cac phan tu co kieu du lieu khac nhau
#len
a = [1, 2, 3, 4]

print(len(a)) 
for i in range(0, len(a)):
    print(a[i], end = ' ')


b = [1, 2, 3, 4, 'hung', 2 + 4j, True]

#for each

for i in b:
    print(type(i))
    


#list constructor
s = 'hung' #chuyen thanh list
c = list(s)
print(c)



#negative index: doi xung voi cac phan tu trong list qua cai guong
d = [1, 2, 3, 4]
print(d[-1]) #negative index bat dau tu -1



""" Them phan tu vao list """
#them phan tu vao cuoi list : append()

e = [1, 2, 3, 4, 5]

e.append('1213')

#them phan tu vao vi tri bat ki : insert(index, value);
e.insert(1, 100) #thay phan tu 2 thanh 100 

print(e)

""" xoa phan tu khoi list """
#pop

e.pop() #xoa phan tu cuoi cung

e.pop(1) #xoa phan tu chi so 1 trong list

print(e)

#del 
del e[1]
print(e)

#remove: phan tu phai co trong mang, remove(value)
f = [1, 2, 3, 4, 2]

f.remove(2) #xoa so 2 dau tien

print(f)

#clear: xoa moi phan tu trong list
f.clear()
print(f)

""" sao chep list """
g = [1, 2, 3]
h = g * 2 #h la 2 lan g
print(h) #[1, 2, 3, 1, 2, 3]

#khai bao mang 1000 phan tu
i = [0] * 1000
print(i)


""" tim kiem phan tu trong list """
#dung toan tu in
j = [1, 'apple', 2, True]

if "apple" in j:
    print("YES")
else:
    print("NO")



""" combine list """
a = [1, 2, 3]
b = [2, 3, 4]

a.extend(b)
print(a)

a += b
print(a)
