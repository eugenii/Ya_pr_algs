# I Любители конференций.
from collections import Counter


def likes(ids_iter, k: int) -> list[int]:
    """
    Вывести k id самых популярных ВУЗов в списке.
    """
    # Подсчёт частот за один проход: O(n)
    counter = Counter(ids_iter)
    if k == 0:
        return []
    
    # Получаем ВСЕ пары, сортируем: сначала по count desc, потом по id asc (стабильно!)
    items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [id_ for id_, _ in items[:k]]

#     ids_dict = {i:ids.count(i) for i in ids}
#     result = sorted(ids_dict.items(), key=lambda x: x[1], reverse=True)[:k]
#     return [i[0] for i in result]


if __name__ == '__main__':
    n = int(input())
    ids = [int(i) for i in input().split()]
    k = int(input())
    print(*likes(ids, k))