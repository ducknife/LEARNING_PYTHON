
def check(n):
    for i in n:
        if i != '4' and i != '7':
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        print('YES' if check(n) else 'NO')