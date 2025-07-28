s = '123,123,12'
t = s.replace('123', '1')
print(t)

a = s.split(',')
print(a)

b = ';'.join(s) #ket hop thanh mot xau hoan chinh
print(b)

#tim kiem
print('123' in s)
print(s.find('123'))

#ham pho bien
print(ord('A')) #ma ascii
print(chr(65)) #thanh ki tu
print('A'.isdigit()) #False
print('A'.isalpha()) #True
print('A'.isalnum()) #True
print('A'.isupper()) #True
print('A'.islower()) #False
print('A'.isspace()) #False: isspace: toan la khoang trang
print('A'.startswith('A')) #True : bat dau bang 'A'
print('A'.endswith('A')) #True: ket thuc bang 'A'

c = "hung rat Dep trai"
print(c.lower()) #chuyen xau thanh chu thuong
print(c.upper()) #chuyen xau thanh chu hoa
print(c.capitalize()) #viet hoa chu cai dau cua xau
print(c.title()) #in hoa chu cai dau cua tung tu trong xau
print(c.swapcase()) #thuong thi doi thanh in hoa, nguoc lai la in thuong
