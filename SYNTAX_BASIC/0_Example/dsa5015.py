import math
MOD = int(1e9) + 7
t = int(input())
for i in range(1, t + 1):
    n, k = map(int, input().split())
    print(math.perm(n, k) % MOD)