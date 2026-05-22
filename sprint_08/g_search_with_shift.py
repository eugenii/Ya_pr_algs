# Поиск со сдвигом.
import sys


def check_pattern(tepmperature: list[int], shift_pattern: list[int]) -> bool:
    for idx in range(len(tepmperature) - 1):
        if tepmperature[idx + 1] - tepmperature[idx] != shift_pattern[idx]:
            return False
    return True


def search_with_shift(tepmperature: list[int], shift_pattern: list[int]) -> list[int]:
    res = []
    for idx in range(len(tepmperature) - len(shift_pattern)):
        if check_pattern(tepmperature[idx:idx + len(shift_pattern) + 1], shift_pattern):
            res.append(idx + 1)
    if res:
        return res
    return [-1]


if __name__ == '__main__':
    data = sys.stdin.read().splitlines()

    n = int(data[0])
    tepmperature = [int(x) for x in data[1].split()]
    pattern_len = int(data[2])
    pattern = [int(x) for x in data[3].split()]

    shift_pattern = []
    for i in range(pattern_len - 1):
        shift_pattern.append(pattern[i + 1] - pattern[i])

    result = search_with_shift(tepmperature, shift_pattern)
    print(*result)

# print(n, tepmperature, pattern_len, pattern, sep='\n')
# print(shift_pattern)

# проверка check_pattern
# print(check_pattern([3, 6, 10, 2], [3, 4, -8]))
# print(check_pattern([0, 0, -2, 0, 5], [0, -2, 2, 5]))
      