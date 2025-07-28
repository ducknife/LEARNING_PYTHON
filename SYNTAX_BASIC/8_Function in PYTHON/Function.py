import math


def sum(a, b): #a, b là tham só hình thức 
    return a + b
print(sum(1, 2)) #1, 2 là đối số = tham số chính thức = Argument

print(sum(b = 1, a = 3))   #keyword argument

# def isPrime(n):
#     a = math.isqrt(n) + 1
#     if n < 2: 
#         return False
#     for i in range(2, a):
#         if n % i == 0:
#             return False
#     return True;
#

def infor(name, id = '1234'):
    print(name, id)
    
if __name__ == '__main__':
    infor('hung', '1123')
    infor('hung') #default argument


