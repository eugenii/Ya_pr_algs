# F Периметр треугольника
"""
Необходимо найти максимальныей пеиметр треугольника, составленного из предложенных сторон.
"""


def f(arr:list[int]) -> int:
    """
    Найти максимальный периметр.
    Args:
        arr (list): список возможных сторон треугольника 

    Returns:
        int: максимальный периметр
    """
    arr.sort(reverse=True)
    for i in range(len(arr) - 2):
        if arr[i] < arr[i + 1] + arr[i + 2]:
            return arr[i] + arr[i + 1] + arr[i + 2]

n = int(input())
arr = [int(i) for i in input().split()]
print(f(arr))

