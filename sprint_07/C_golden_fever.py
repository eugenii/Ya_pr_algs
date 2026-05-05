# C Золотая лихорадка.
import sys

data = sys.stdin.read().split()

bag = int(data[0])
n = int(data[1])

cost = 0

heaps = []
# heaps = [(c, m) for c, m in zip(data[2::2], data[3::2])]
idx = 2
for _ in range(n):
    c = int(data[idx])
    m = int(data[idx + 1])
    heaps.append((c, m))
    idx += 2
# Сортируем кучи по убыванию стоимости за 1 кг
heaps.sort(key=lambda x: x[0], reverse=True)

for heap in heaps:
    if bag <= 0:
        break

    take_mass = min(bag, heap[1])
    bag -= take_mass
    cost = cost + take_mass * heap[0]

print(cost)
