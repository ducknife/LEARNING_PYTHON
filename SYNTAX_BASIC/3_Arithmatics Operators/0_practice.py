#Toán tử gán
a = 10
b = 100
b, a = a, b #Hoán vị a, b
print(b, a, sep=' ') #10, 100

#Toán tử số học
print(a * b)
print(a ** b)
print(a / b) #chia kết quả là số thực 
print(a // b) #chia kết quả chỉ lấy phần nguyên 
print(a - b)
print(a + b)

#Toán tử bit

print(a | b) #a or b
print(a & b) #a and b
print(a ^ b) #a xor b
print(~a) #not a = -a - 1

#Toán tử nhận dạng

if a is b:
    print("YES a is b")
else:
    print("NO a is not b")

if a is not b:
    print("YES a is not b")
else:
    print("NO a is b")


#Toán tử member 

s = '''Hung
rat la dep trai va skibidi'''

t = 'skibidi'

u = 'dop dop yes yes'

if t in s:
    print("YES t is in s")
else:
    print("NO t is not in s")

if u not in s:
    print("YES u is not in s")
else:
    print("NO u is in s")