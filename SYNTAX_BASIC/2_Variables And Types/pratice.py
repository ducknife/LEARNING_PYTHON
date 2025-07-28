a = 0
b = 1.12
c = 'Hung'
d = True
e = False
f = 2 + 3j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#
g = 12.3123

print(bool(g)) # == true if g != 0 || g != '';
print()

# xau nhieu dong
h = '''Hung 
ten la hung'''

print(h)

# ep kieu

i = 2134.12312

print(int(i))

j = '112.1231233'
print(float(j))

print(str(i))
print(str(j))


""" Kiểu dữ liệu trong python """
a = 10 # int
b = 12.6 # float
c = 'Hung' # str
d = 3 + 5j # complex
e = True # bool
f = False # bool

""" ép kiểu: data_type(object) """

string = '12.3123'
float = float(string)
print(float) # 12.3123

string2 = '12'
integer = int(string2)
print(integer) # 12