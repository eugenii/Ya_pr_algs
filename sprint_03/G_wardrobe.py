# G Гардероб.

"""
Необходимо отсортировать массив с повторяющимися элементами за 1 проход.
"""

def sort_colors(nums):
    """
    Отсортировать массив за 1 проход.
    Реализация DUTCH NATIONAL FLAG (Dijkstra)
    """
    if not nums:
        return []

    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1    #  mid не меняем, так как там может быть 1
    return nums


def test():
    arr = [2, 0, 2, 1, 1, 0]
    assert sort_colors(arr) == [0, 0, 1, 1, 2, 2]


n = int(input())
nums = [int(i) for i in input().split()]
print(*sort_colors(nums))