# Финальное задание спринта 8 Packed Prefix
# Yandex Context solution ID https://contest.yandex.ru/contest/26133/run-report/162603350/    ( 162560959 )
# Временная сложность (Time Complexity):
# O(N * L), где N — число строк, а L — максимальная длина распакованной строки (до 10^5). 
# Мы тратим время на распаковку каждой строки и её посимвольное сравнение с префиксом.
# Пространственная сложность (Space Complexity): O(L). 
# В памяти одновременно хранятся только базовый префикс и одна текущая распаковываемая строка. 
# Стек для распаковки занимает ничтожно мало, так как исходные запакованные строки короткие.

import sys


NUMBERS = set("0123456789")


def unpack_string(compressed_str: str) -> str:
    """Распаковывает запакованную строку (ЗС) по правилу n[A]."""
    stack: list[tuple[str, int]] = []
    current_str: str = ""
    current_num: str = ""

    for symb in compressed_str:
        if symb in NUMBERS:
            current_num = current_num + symb
        elif symb == '[':
            stack.append((current_str, int(current_num)))
            current_str = ""
            current_num = ""
        elif symb == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += symb

    return current_str


def find_longest_common_prefix(strings_count: int, lines_iterator) -> str:
    """Находит наибольший общий префикс для N распакованных строк."""
    if strings_count == 0:
        return ""

    try:
        first_line = next(lines_iterator).strip()
    except StopIteration:
        return ""
        
    common_prefix: str = unpack_string(first_line)

    for _ in range(1, strings_count):
        try:
            line = next(lines_iterator).strip()
        except StopIteration:
            break
            
        current_str: str = unpack_string(line)
        
        if len(current_str) < len(common_prefix):
            common_prefix = common_prefix[:len(current_str)]

        for i in range(len(common_prefix)):
            if common_prefix[i] != current_str[i]:
                common_prefix = common_prefix[:i]
                break
                
        if not common_prefix:
            return ""

    return common_prefix


if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()
    if input_data:
        n = int(input_data[0])
        lines = iter(input_data[1:])
        print(find_longest_common_prefix(n, lines))
