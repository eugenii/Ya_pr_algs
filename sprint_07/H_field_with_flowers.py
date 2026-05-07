# H field with flowers.
import sys

data = sys.stdin.read().split()

n, m = int(data[0]), int(data[1])

field = []
for line in data[2:]:
    field.append([int(j) for j in list(line)])

dp = [[0 for _ in range(m)] for _ in range(n)]  
dp[n - 1][0] = field[n - 1][0]

for i in range(n - 1, -1, -1):
    for j in range(m):
        if i == n - 1 and j == 0:
            continue
        if i == n - 1:
            dp[i][j] = dp[i][j - 1] + field[i][j]
            continue
        elif j == 0:
            dp[i][j] = dp[i + 1][j] + field[i][j]
            continue
        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + field[i][j]
# print(data[2:])
# print(dp, sep='\n')
# print(field)
print(dp[0][m - 1])