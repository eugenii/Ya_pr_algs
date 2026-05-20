# Вставка строк.
import sys



def solve():
    data = sys.stdin.read().splitlines()
    if not data:
        return 
    
    s = data[0]
    n = int(data[1])

    # Хранилище вставок: ключ — индекс в s, значение — строка для вставки
    # k_i может быть от 0 до len(s)
    insertions = {}

    for i in range(2, 2 + n):
        t_i, k_i = data[i].split()
        insertions[int(k_i)] = t_i

    result = []

    # Шаг 1: Проверяем вставку в самое начало (k_i == 0)
    if 0 in insertions:
        result.append(insertions[0])

    # Шаг 2: Идем по строке s и вставляем подарки ПОСЛЕ нужного символа
    # В Python строки индексируются с 0, поэтому символ с номером k_i имеет индекс k_i - 1.
    # Проще: итерируемся по символам s. Индекс 0 в s соответствует позиции вставки k_i = 1.
    for idx, char in enumerate(s):
        result.append(char)
        current_k = idx + 1
        if current_k in insertions:
            result.append(insertions[current_k])

    # Шаг 3: Собираем финальную строку за один проход O(N)
    print("".join(result))


if __name__ == "__main__":
    solve()





# Плохой вариант:
# В чем проблема текущего решения?
# Сортировка внутри цикла: Строка strings.sort(...) находится внутри цикла for. 
# Из-за этого список сортируется заново на каждом шагу ввода. 
# При \(N = 10^5\) это превращается в миллиарды лишних операций. 
# Сортировку нужно вынести за пределы цикла ввода.
# Слайсы строки в цикле: Операции line[:...] и head + s[0] + tail создают новую строку в памяти на каждой итерации.
# Так как длина строки растет до сотен тысяч символов, постоянное копирование памяти намертво вешает программу.

# line = input()
# base = 0

# strings = []
# for i in range(int(input())):
#     strings.append(input().split())
#     strings.sort(key=lambda x: int(x[1]))

# print(strings)

# for s in strings:
#     head = line[: int(s[1]) + base]
#     tail = line[int(s[1]) + base:]
#     line = head + s[0] + tail
#     base += len(s[0])
#     # print(line)


# assert line == 'dequeabqueueacabastack'