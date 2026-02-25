# J Сортировка пузырьком.

n = int(input())
data = [int(i) for i in input().split()]

was_ever_swapped = False # Была ли хоть одна замена за всё время

for i in range(n - 1):
    changed = False # Была ли замена в текущем проходе
    for j in range(n - 1 - i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            changed = True
            was_ever_swapped = True
    
    if changed:
        print(*data)
    else:
        # Если замен в этом проходе не было, значит массив отсортирован
        break

# Если за всё время работы не было ни одной замены (массив сразу был ок)
if not was_ever_swapped:
    print(*data)