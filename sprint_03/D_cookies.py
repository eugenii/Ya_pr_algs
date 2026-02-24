# D Печеньки.

n = int(input())    # Количество детей
greed = [int(i) for i in input().split()]

m = int(input())    # Количество печенек
cookies = [int(i) for i in input().split()]

result = 0
child_pos = 0

# Сортируем всё.

greed.sort()
cookies.sort()

# Перебираем печенье.
for cookie in cookies:
    if cookie >= greed[child_pos]:
        result += 1
        child_pos += 1
        if child_pos == n:
            break

print(result)

