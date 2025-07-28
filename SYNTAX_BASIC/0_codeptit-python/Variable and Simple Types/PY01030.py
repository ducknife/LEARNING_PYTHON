import math

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    n, k = map(int, input().split())
    x = pow(10, k)
    cnt = 0
    for i in range(pow(10, k - 1), x):
        if math.gcd(i, n) == 1:
            cnt += 1
            print(i, end=' ')
            if cnt == 10:
                print()
                cnt = 0