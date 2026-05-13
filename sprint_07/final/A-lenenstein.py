# A lenenstein

s, t = input(), input()

dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

for i in range(len(s) + 1):
    dp[i][0] = i

for j in range(len(t) + 1):
    dp[0][j] = j

for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i - 1] == t[j - 1]:
            # Буквы совпали — стоимость операции 0, берём значение по диагонали
            dp[i][j] = dp[i - 1][j - 1]
        else:
            # Буквы разные — выбираем минимальный путь из трёх соседей и добавляем 1
            dp[i][j] = 1 + min(
                dp[i - 1][j],     # Удаление
                dp[i][j - 1],     # Вставка
                dp[i - 1][j - 1]  # Замена
            )

print(dp[len(s)][len(t)])
