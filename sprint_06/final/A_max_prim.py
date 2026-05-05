# Успешная посылка: https://contest.yandex.ru/contest/25070/run-report/160819763/
# Алгоритм:
# Использован алгоритм Прима с приоритетной очередью (min-heap). 
# Для нахождения максимального дерева веса рёбер инвертировались 
# (умножались на -1), так как стандартная куча в Python работает на минимум.
# Временная сложность: O(M * log M) или O(M * log N).
# Мы проходим по каждому ребру один раз и добавляем его в приоритетную очередь. 
# Операция вставки и удаления из кучи занимает O(log M).
# Поскольку M  в худшем случае пропорционально N^2 , это даёт нам эффективную 
# работу даже на плотных графах.
# Пространственная сложность: O(N + M).
# O(N + M)  требуется для хранения списка смежности.
# O(M) требуется для хранения рёбер в приоритетной очереди в худшем случае.
# O(N) для массива посещённых вершин.
# Для эффективного чтения большого объёма использован стандартый sys.stdin.read()

import sys
import heapq


def solve():
    # Быстрое чтение
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Случай с пустой сетью
    if n == 0:
        print(0)
        return

    adj = [[] for _ in range(n + 1)]
    cursor = 2
    for _ in range(m):
        u = int(input_data[cursor])
        v = int(input_data[cursor + 1])
        w = int(input_data[cursor + 2])
        # Игнорируем петли, они не нужны для остова
        if u != v:
            adj[u].append((v, w))
            adj[v].append((u, w))
        cursor += 3

    not_visited = [True] * (n + 1)
    pq = []
    max_mst_weight = 0
    added_count = 0

    def add_node(v):
        nonlocal added_count
        not_visited[v] = False
        added_count += 1
        for neighbor, weight in adj[v]:
            if not_visited[neighbor]:
                # Инвертируем вес, чтобы heapq выдавал максимум
                heapq.heappush(pq, (-weight, neighbor))

    # Начинаем с любой вершины, например с 1
    add_node(1)

    while pq and added_count < n:
        neg_weight, v = heapq.heappop(pq)
        if not_visited[v]:
            max_mst_weight += (-neg_weight)
            add_node(v)

    # Проверка на связность
    if added_count == n:
        print(max_mst_weight)
    else:
        print("Oops! I did it again")


if __name__ == '__main__':
    solve()
