# Микрозадача на ДП и поиск слов

T = "pygo"

words = ["py", "go", "p"]

dp = [False] * (len(T) + 1)
dp[0] = True

for i in range(len(T)):
    if dp[i]:
        for word in words:
            if T[i: i + len(word)] == word:
                dp[i + len(word)] = True

print(dp[-1])