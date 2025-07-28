#tuong tu map trong c++, key-value
#moi key la duy nhat
#tao dict
userData = {
    'name' : 'Hung',
    'age' : 20,
    'major': 'IT',
    'job' : 'AI engineering',
}

print(userData['name']) #chỉ dùng khi đã có key trong dict
print(userData.get('name')) # chưa có key sẽ trả về None 

print(userData.keys()) #in ra cac key
print(userData.values()) #in ra cac value
print(userData.items()) #in ra cac cap

for key, value in userData.items():
    print(key, value)

#zip
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = dict(zip(a, b))
print(c)

#fromkeys
d = dict.fromkeys(a, 1)
print(d)
#tim kiem key, value
print('job' in userData.keys()) #O(1)
print('Hung' in userData.values()) #O(n)

#them key va value
userData['status'] = 'single'
print(userData) 

userData['status'] += ' literally'

userData.setdefault('girl friend name', 'Pham Quynh') #thêm key, value nếu key chưa có

#thay doi value
userData['age'] = 21
print(userData['age'])

userData.update({'status': 'date'}) #vừa thêm vừa sửa được nhiều phần tử

#xoa phan tu trong dictionary
del userData['major']
print(userData)

userData.pop('job')
print(userData)

userData.popitem()
print(userData)

userData.clear()
print(userData)


