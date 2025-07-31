#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    s = list(input())
    s = s[::-1]
    while len(s) > 1 and s[-1] == '0':
        s.pop()
    s = s[::-1]
    n = len(s)
    res = ''
    cnt = 0
    for i in range(n - 1, -1, -1):
        cnt += 1
        res += s[i]
        if i == 0:
            break
        if cnt % 3 == 0:
            res += ','
            cnt = 0
    print(res[::-1])