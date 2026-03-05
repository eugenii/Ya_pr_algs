# H Большое число.

def is_less(a: str, b: str) -> bool:
    """
    Возвращает True, если комбинация (a + b) меньше, чем (b + a).
    Это значит, что 'a' должно стоять ПОСЛЕ 'b' для получения максимума.
    """
    return a + b < b + a

def big_number(data: list[str]) -> str:
    for i in range(1, len(data)):
        item = data[i]
        j = i
        # Сдвигаем элементы, пока текущий item "лучше" (больше при склейке), 
        # чем элемент слева (data[j-1])
        while j > 0 and is_less(data[j - 1], item):
            data[j] = data[j - 1]  # Сдвигаем соседа вправо
            j -= 1
        data[j] = item  # Ставим наш элемент на освободившееся место
    
    return ''.join(data)

if __name__ == '__main__':
    _ = input()
    data = input().split()
    print(big_number(data))
    