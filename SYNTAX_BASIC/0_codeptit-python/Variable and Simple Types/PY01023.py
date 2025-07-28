import math

DUCKNIFE = '__main__'

def ptich(n):
    x = math.isqrt(n) + 1
    di = {i : 0 for i in range(0, x)}
    for i in range(2, x):
        while n % i == 0:
            di[i] += 1
            n //= i
    if n > 1:
        di[n] = 1
    a = []
    print(1, end=' * ')
    for i, fi in di.items():
        if fi > 0:
            a.append((i, fi))
    for i in range(0, len(a)):
        print(a[i][0], '^', a[i][1], sep='', end=' ')
        if i < len(a) - 1:
            print('*', end=' ')
    print()

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        n = int(input())
        ptich(n)
