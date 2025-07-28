
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input()
        a = list(map(int, str))
        n = len(a)
        for i in range(n - 1, 0, -1):
            if a[i] >= 5:
                a[i] = 0
                a[i - 1] += 1
            else:
                a[i] = 0
        for i in a:
            print(i, end='')
        print()