
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c = map(float, input().split())
        for i in range(0, 1000):
            if a * pow(1 + b / 100, i) >= c:
                print(i)
                break
        