#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        s = input()
        a = []
        for i in s:
            a.append(ord(i))
        a2 = a[::-1]
        n = len(a)
        check = True
        for i in range(1, n):
            if abs(a[i] - a[i - 1]) != abs(a2[i] - a2[i - 1]):
                check = False
        print('YES' if check else 'NO') 