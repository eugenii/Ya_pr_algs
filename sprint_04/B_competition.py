# B соревнование

n = int(input())
arr = list(map(int, input().split()))

# Словарь: {значение_баланса: первый_индекс_где_оно_встретилось}
# Изначально баланс 0 на "виртуальном" индексе -1 (перед началом)
first_occurrence = {0: -1}

balance = 0
max_length = 0

for i in range(n):
    if arr[i] == 0:
        balance -= 1
    else:
        balance += 1
    # Если такой баланс уже был, считаем длину отрезка
    if balance in first_occurrence:
        max_length = max(max_length, i - first_occurrence[balance])
    # Если такой баланс встретили впервые, запоминаем его индекс
    else:
        first_occurrence[balance] = i

print(max_length)