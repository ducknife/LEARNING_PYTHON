#import ...

DUCKNIFE = '__main__'

if __name__ == DUCKNIFE:
    #ducknife
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        for i in range(0, n):
            if s[i].isdigit():
                for j in range(0, int(s[i])):
                    print(s[i - 1], end='')
        print()