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
      
# Решение от Google AI
# Передаем индексы, избегая копирования памяти через срезы
def check_pattern(
    temperature: list[int], start_idx: int, shift_pattern: list[int]
) -> bool:
    for idx in range(len(shift_pattern)):
        # Сравниваем элементы прямо в исходном массиве
        current_diff = (
            temperature[start_idx + idx + 1] - temperature[start_idx + idx]
        )
        if current_diff != shift_pattern[idx]:
            return False
    return True


def search_with_shift(
    temperature: list[int], shift_pattern: list[int]
) -> list[int]:
    res = []
    # Если шаблон состоит из 1 элемента, разностей нет — он подходит везде
    if not shift_pattern:
        return list(range(1, len(temperature) + 1))

    # Длина окна разностей на 1 меньше, чем длина исходного шаблона
    for idx in range(len(temperature) - len(shift_pattern)):
        if check_pattern(temperature, idx, shift_pattern):
            res.append(idx + 1)
    return res if res else [-1]
