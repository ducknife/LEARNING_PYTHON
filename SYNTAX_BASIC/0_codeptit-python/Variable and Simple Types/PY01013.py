import math

DUCKNIFE = '__main__'

def is_prime(n):
    if n < 2:
        return False
    x = math.isqrt(n) + 1
    for i in range(2, x):
        if n % i == 0:
            return False
    return True

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        c = math.gcd(a, b)
        d = str(c)
        sum = 0
        for i in d:
            sum += int(i)
        print('YES' if is_prime(sum) else 'NO')