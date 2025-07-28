
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input()
        a = str[0:2]
        b = str[len(str) - 2:len(str)]
        print('YES' if a == b else 'NO')