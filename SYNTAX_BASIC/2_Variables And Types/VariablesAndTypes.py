#python can auto detect type of variable

a = 10 #integer
b = 12.6 #floating-point number
c = 'hung' #string
d = 5 + 3j #complex
e = True
f = False

print(type(a)) #<class 'int'>
print(type(b)) #<class 'float'>
print(type(c)) #<class 'str'>
print(type(d)) #<class 'complex'>

# if float x > float_max => x = inf
# else if float x < float_min => x = 0

t = 28.02394234
print('%.2f' % t) #28.02

# if e != "" and e != 0
print(bool(t)) #True

#Xau gom nhieu dong khi dung '''s'''
s = '''python 
with
ducknife''' 
print(s)

#Ep kieu
m = '123'
a = int(m)
print(a)
print(int(m) + 1)

print(float(a))

#sang string
a = True
s = str(a) 
print(s)
b = 123.23
s = str(b)
print(s)
c = 231234
s = str(c)
print(c)