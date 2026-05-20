# Разворот строки.

def reverse_string(line: str) -> str:
    words = line.split()
    return ' '.join(words[::-1])


if __name__ == '__main__':
    line = input()
    print(reverse_string(line))