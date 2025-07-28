#import ...

DUCKNIFE = '__main__'

P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

if __name__ == DUCKNIFE:
    #ducknife
    while True:
        s = input()
        if s == '0':
            break
        t, st = s.split()
        n, k = len(st), int(t)
        res = ''
        for i in range(0, n):
            idx = P.index(st[i])
            idx = (idx + k) % 28
            res += P[idx]
        print(res[::-1])