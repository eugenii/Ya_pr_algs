# D Полиноминальный хеш.


def polynomial_hash(a, m, s):
    h_s = 0
    for i in range(len(s)):
        h_s = (h_s * a + ord(s[i])) % m
    return h_s

a = int(input())  # Основание.
m = int(input())  # Модуль.
s = input()       # Строка.

print(polynomial_hash(a, m, s))
