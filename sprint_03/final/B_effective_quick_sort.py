# B Эффективная быстрая сортировка.


def comparator(a:tuple[str, int, int], b:tuple[str, int, int]) -> bool:
    """
    Возвращает True, если a < b.
    """
    pass

def partition(array:list[tuple[str, int, int]], pivot:tuple[str, int, int]):
    """
    Возвращает массив, разбитый на три части:
    - левая часть содержит все значения, меньшие pivot
    - средняя часть содержит все значения, равные pivot
    - правая часть содержит все значения, большие pivot
    """
    pass

def quicksort(array:list[tuple[str, int, int]]):
    pass


n = int(input())
arr = []
for i in range(n):
    name, score, penalti = input().split()
    arr.append((name, int(score), int(penalti)))
print(*arr, sep='\n')

quicksort(arr)
print(*arr, sep='\n')