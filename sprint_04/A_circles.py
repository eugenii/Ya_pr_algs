# A Кружки.
# -*- coding: utf-8 -*-


import sys
import io

# Устанавливаем кодировку для стандартного ввода и вывода
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main(n):
    result = dict()
    for _ in range(n):
        if (name := input()) in result:
            result[name] += 1
        else:
            result[name] = 1
    return list(result.keys())
    

if __name__ == '__main__':
    n = int(input())
    print(*main(n), sep='\n')
