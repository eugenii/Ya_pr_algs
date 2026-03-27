# Различные деревья поиска.

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for k in range(2, n + 1):
    for i in range(1, k + 1):
        dp[k] += dp[i - 1] * dp[k - i]

print(dp[n])