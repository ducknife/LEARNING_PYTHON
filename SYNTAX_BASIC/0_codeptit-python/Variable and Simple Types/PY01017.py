#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        s += '$'
        cnt = 0
        for i in range(0, n):
            cnt += 1
            if s[i] != s[i + 1]:
                print(cnt, s[i], sep='', end='')
                cnt = 0
        print()