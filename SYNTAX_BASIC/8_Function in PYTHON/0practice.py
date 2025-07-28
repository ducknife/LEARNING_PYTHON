import math

def gcd(a, b):
    return math.gcd(a, b)

print(gcd(10, 2))
 
print(gcd(a = 10, b = 5)) #keyword argument
print(gcd(b = 110, a = 5))

def info(name, age = 20):
    print(name, age, sep=' ')

info('Hung') #default
info('Hung', '1000')

#main function

if __name__ == '__main__':
    info('Day la ham main goi ham info voi ten la dong nay va tuoi la:', 20)


#vi du kiem tra so nguyen to

n = int(input())

def isPrime(a):
    end = math.isqrt(a) + 1
    if a < 2: 
        return False
    for i in range(2, end):
        if a % i == 0:
            return False
    return True

if isPrime(n):
    print("n is a prime")
else:
    print("n is not a prime")


""" lambda function """
sum = lambda x, y : x + y
print(sum(2, 1))

a = [1, 2, 3]
b = list(map(lambda x : x ** 2, a))
print(b)

c = list(filter(lambda x : x % 2 == 1, a))
print(c)

MAXOF = lambda x, y : x if x > y else y
print(MAXOF(2, 12))


