import random

random.seed(10) # dùng để sinh dữ liệu giống như dữ liệu đã sinh ở lần sinh trước đó
# seed(x) : x khác nhau cho ra kết quả khác nhau 

print('for 1st')
for i in range(100):
    print(random.randint(10, 100), end=', ' if i < 99 else '\n')

print('for 2nd')
random.seed(10)
for i in range(100):
    print(random.randint(10, 100), end=', ' if i < 99 else '\n')

random.seed(12)
print('random x 1st')
x = random.randint(10, 1000)
print(x)

print('random x 2nd')
random.seed(12)
y = random.randint(10, 1000)
print(y)



