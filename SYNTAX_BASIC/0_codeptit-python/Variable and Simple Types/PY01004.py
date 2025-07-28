import math

def is_prime(n):
    if n < 2:
        return False
    x = math.isqrt(n)
    for i in range(2, x + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for i in range(1, n):
            if math.gcd(i, n) == 1:
                cnt += 1
        if is_prime(cnt) == True:
            print('YES')
        else:
            print('NO')
            