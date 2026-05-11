# J Путешестиве.
import sys

data = sys.stdin.read().split()

n = int(data[0])

dp = [1] * n
prev = [-1] * n

# 1. Выделяем только рейтинги и превращаем в числа
ratings = [int(x) for x in data[1:]] 

for i in range(n):
    for j in range(i):
        if ratings[j] < ratings[i]:
            # Обновляем, только если нашли цепочку длиннее текущей
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

# 2. Ищем максимальную длину цепочки
max_len = max(dp)
cur_idx = dp.index(max_len)

# 3. Идём по цепочке назад.
path = []
while cur_idx != -1:
    path.append(cur_idx + 1)  # Добавляем ПОРЯДКОВЫЙ НОМЕР (индекс + 1)
    cur_idx = prev[cur_idx]   

# 4. Разворачиваем путь
path.reverse()

print(len(path))
print(*path)
