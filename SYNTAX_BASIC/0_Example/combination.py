import math

t = int(input())
for i in range(1, t + 1):
    n, m = map(int, input().split())
    print(math.comb(n, m))