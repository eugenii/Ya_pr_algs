# B Эффективная быстрая сортировка.
"""
Успешное решение: https://contest.yandex.ru/contest/23815/run-report/158042138/

Принцип работы
Алгоритм основан на стратегии «разделяй и властвуй»:
- Выбор опорного элемента (pivot). Берём средний элемент: array[(start + end) // 2].
- Разбиение массива вокруг pivot: элементы меньше или равные pivot перемещаются влево, большие — вправо.
- Рекурсивная сортировка левой и правой частей массива.

Базовое условие рекурсии: 
- если start >= end, массив уже отсортирован (пустой или один элемент).

Инициализация указателей: 
- left = start, right = end.

Поиск элементов для обмена:
Двигаем left вправо, пока array[left] < pivot (ищем элемент, который должен быть справа от pivot).
Двигаем right влево, пока array[right] > pivot (ищем элемент, который должен быть слева от pivot).
Обмен элементов: если left <= right, меняем array[left] и array[right] местами, сдвигаем указатели (left += 1, right -= 1).

Рекурсивный вызов: сортируем левую часть (start до right) и правую часть (left до end).

Сложность по времени: 
Лучший случай: O(n logn) - когда pivot выбран оптимально (близко к середине).
Худший случай O(n^2) - когда pivot выбран не оптимально (всего либо слева, либо справа).

Сложность по памяти: O(1), так как не используется дополнительная память, замена происходит
в исходном массиве (in-place). В худшем случае O(n) - из-за рекурсии.
"""


def compare(a:tuple[int, int, str], b:tuple[int, int, str]) -> bool:
    """
    Возвращает True, если a < b.
    """
    return a < b


def quick_sort(array, start, end):
    """
    Quick sort.
    """
    if start >= end:
        return

    # Выбираем пивот (например, посередине)
    pivot = array[(start + end) // 2]
    left, right = start, end

    while left <= right:
        # Ищем элемент слева, который должен быть справа
        while compare(array[left], pivot): # array[left] < pivot
            left += 1
        # Ищем элемент справа, который должен быть слева
        while compare(pivot, array[right]): # array[right] > pivot
            right -= 1
        
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    # Рекурсивно запускаем для левой и правой части
    quick_sort(array, start, right)
    quick_sort(array, left, end)


def main():
    n = int(input())
    arr = []
    for i in range(n):
        name, tasks, penalti = input().split()
        arr.append((-int(tasks), int(penalti), name))
    quick_sort(arr, 0, len(arr)-1)
    for member in arr:
        print(member[2])


if __name__ == '__main__':
    main()