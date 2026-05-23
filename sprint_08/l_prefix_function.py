# Подсчёт префикс-функции.

def prefix_function(s):
    # Функция возвращает массив длины |s|
    n = len(s)
    π = [None] * n
    π[0] = 0
    for i in range(1, n):
        k = π[i - 1]
        while k > 0 and s[k] != s[i]:
            k = π[k - 1]
        if s[k] == s[i]:
            k += 1
        π[i] = k
    return π


s = input()
print(*prefix_function(s))