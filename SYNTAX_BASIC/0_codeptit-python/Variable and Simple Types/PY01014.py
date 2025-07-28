#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    a, k, n = map(int, input().split())
    m = n // k + 1
    check = False
    for i in range(1, m):
        if i * k - a > 0:
            print(i * k - a, end=' ')
            check = True
    if not check:
        print(-1)
    else:
        print()
        