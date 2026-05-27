# Финальное задание спринта 8 Packed Prefix
# Yandex Context solution ID 162560959
# Временная сложность (Time Complexity):
# O(N * L), где N — число строк, а L — максимальная длина распакованной строки (до 10^5). 
# Мы тратим время на распаковку каждой строки и её посимвольное сравнение с префиксом.
# Пространственная сложность (Space Complexity): O(L). 
# В памяти одновременно хранятся только базовый префикс и одна текущая распаковываемая строка. 
# Стек для распаковки занимает ничтожно мало, так как исходные запакованные строки короткие.

import sys


def unpack_string(compressed_str: str) -> str:
    """Распаковывает запакованную строку (ЗС) по правилу n[A]."""
    stack: list[tuple[str, int]] = []
    current_str: str = ""
    current_num: int = 0

    for char in compressed_str:
        if char.isdigit():
            # Так как числа однозначные, можно просто приравнять
            # В курсе python разработчик была у меня такая задача - там число набирал умножением.. 
            current_num = int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str


def find_longest_common_prefix(strings_count: int, lines_iterator) -> str:
    """Находит наибольший общий префикс для N распакованных строк."""
    if strings_count == 0:
        return ""

    # Распаковываем самую первую строку и берём её за эталонный префикс
    try:
        first_line = next(lines_iterator).strip()
    except StopIteration:
        return ""
        
    common_prefix: str = unpack_string(first_line)

    # Поочередно обрабатываем остальные строки
    for _ in range(1, strings_count):
        try:
            line = next(lines_iterator).strip()
        except StopIteration:
            break
            
        current_str: str = unpack_string(line)
        
        # Обрезаем общий префикс до длины текущей строки, если она короче
        if len(current_str) < len(common_prefix):
            common_prefix = common_prefix[:len(current_str)]
            
        # Сравниваем посимвольно текущую строку с префиксом
        for i in range(len(common_prefix)):
            if common_prefix[i] != current_str[i]:
                common_prefix = common_prefix[:i]
                break
                
        # Если общий префикс сократился до пустой строки, продолжать нет смысла
        if not common_prefix:
            return ""

    return common_prefix


if __name__ == "__main__":
    # Читаем все данные из sys.stdin эффективным итератором
    input_data = sys.stdin.read().splitlines()
    if input_data:
        n = int(input_data[0])
        lines = iter(input_data[1:])
        print(find_longest_common_prefix(n, lines))
