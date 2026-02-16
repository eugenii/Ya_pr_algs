# L  Числа Фиббоначи по модулю

def fib(n, k):
    mod =  10 ** k
    first, second = 1, 1
    if n in (0, 1):
        return 1
    for i in range(2, n + 1):
        first, second = second, (first + second) % mod
    return second


n, k = map(int, input().split())
print(fib(n, k))