#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        n = input()
        check = True
        for i in range(0, len(n) - 1):
            if n[i] > n[i + 1]:
               check = False
        print('YES' if check else 'NO') 