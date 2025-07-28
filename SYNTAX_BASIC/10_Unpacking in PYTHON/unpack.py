""" 1. unpacking và List """
data = ['Hung', 'dep trai', 19, 'IT']
name, feature, age, major = data
print(name, feature, age, major)


""" 2. unpacking và Tuple """
dataTuple = ('name', 'age', 'number')
mt1, mt2, _ = dataTuple
print(mt1, mt2)


""" 3. unpacking và Range """
a, b, c = range(0, 5, 2)
print(a, b, c) #0, 2, 4


""" 4. unpacking và Set """
dataSet = {'C++', 'Python', 'C'}
pro1, pro2, pro3 = dataSet
print(pro1, pro2, pro3)


""" 5. unpacking và String """
dataString = "Hung"
a, b, c, _ = dataString
print(a, b, c)


""" 6. unpacking và for """
listList = [[1, 2], [2, 3], [3, 4]]
for first, second in listList:
    print(first, second)

""" 7. unpacking khi có nhiều phần tử """
#với list
list = [1, 2, 3, 4, 4, 41, 3211];

x, *y, z = list #x là phần tử đầu tiên, z là phần tử cuối cùng, y là các phần tử còn lại ở giữa
print(x) 
print(y)
print(z)

*x, y, z = list #lấy ra hai phần tử cuối
print(x)
print(y)
print(z)

#với string
string = '''Hung dep
trai vcl'''
x, y, *z = string
print(x, y) #H u

#với tuple
tuple = ((1, 2, 3), (2, 4, 3, 33), (5, 6, 3, 33, 3, 3))
for first, second, *el in tuple:
    print(first, second)


