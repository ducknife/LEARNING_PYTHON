import math

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        n = input()
        n1 = n[::-1]
        print('YES' if math.gcd(int(n), int(n1)) == 1 else 'NO')