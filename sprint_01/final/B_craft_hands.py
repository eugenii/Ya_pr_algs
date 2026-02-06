# Ссылка на отчёт о решении:
# https://contest.yandex.ru/contest/22450/run-report/156206028/

field_dict = dict()
result = 0
FIELD_SIZE = 4

# Считали k и игровое поле
k = int(input())
for i in range(FIELD_SIZE):
    line = input()
    for symb in line:
        if symb in field_dict:
            field_dict[symb] += 1
            continue
        field_dict[symb] = 1

# print(*field_dict.items())   # Проверка  для отладки

# Подсчитаем очки для каждого раунда (t = 0 ... 9, t - переменная из условия задачи)

for t in range(1, 10):
    digit = str(t)
    if digit in field_dict and field_dict[digit] <= k * 2:
        result += 1

print(result)