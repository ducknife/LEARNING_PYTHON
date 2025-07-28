#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    s = input()
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