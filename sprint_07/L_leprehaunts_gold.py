# L Leprehaunts Gold
import sys

data = sys.stdin.read().split()
n = int(data[0])
M = int(data[1])

gold = [int(x) for x in data[2:]]

dp = [0] * (n)
dp[0] = gold[0]

for i in range(1, n):
    max_gold = gold[i]
    for j in range(i - 1, -1, -1):
        if gold[j] + max_gold <= M:
            max_gold += gold[j]
    dp[i] = max(max_gold, dp[i - 1])

print(dp[n - 1])
