
def check(n):
    s = str(n)
    if s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 == 1:
            return False
    if len(s) % 2 == 1:
        return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        for i in range(22, int(n)):
            if check(i):
                print(i, end=' ')
        print()
        