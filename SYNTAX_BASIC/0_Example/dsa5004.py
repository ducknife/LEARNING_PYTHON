n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(0, n):
    dp[i] = 1
    for j in range(0, i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))