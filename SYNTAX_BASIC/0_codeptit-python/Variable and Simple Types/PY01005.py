
if __name__ == '__main__':
    n = input()
    n4, n7 = 0, 0
    for i in n:
        if i == '4':
            n4 += 1
        elif i == '7':
            n7 += 1
    if n4 + n7 == 4 or n4 + n7 == 7:
        print('YES')
    else:
        print('NO')