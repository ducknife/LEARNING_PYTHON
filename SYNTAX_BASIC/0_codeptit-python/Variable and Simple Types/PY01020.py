#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        a = s[n-2:n]
        print('YES' if a == '86' else 'NO')