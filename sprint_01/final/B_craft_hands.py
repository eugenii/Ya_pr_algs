# Ссылка на отчёт о решении:
# https://contest.yandex.ru/contest/22450/run-report/156206028/

field_dict = dict()
res = 0

# Считали k и игровое поле
k = int(input())
for i in range(4):
    line = input()
    for symb in line:
        if symb in field_dict:
            field_dict[symb] += 1
            continue
        field_dict[symb] = 1

# print(*field_dict.items())   # Проверка  для отладки

# Подсчитаем очки для каждого раунда (t = 0 ... 9)

for t in range(1, 10):
    c = str(t)
    if c in field_dict and field_dict[c] <= k * 2:
        res += 1

print(res)