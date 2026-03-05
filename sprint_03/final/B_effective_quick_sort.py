# B Эффективная быстрая сортировка.


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