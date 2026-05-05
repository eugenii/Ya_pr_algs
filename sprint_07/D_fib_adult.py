# D Фибоначчи для взрослых.

MOD = 10**9 + 7


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 1, 1
    for i in range(2, n + 1):
        f_next = (a + b) % MOD
        a, b = b, f_next
    return f_next


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()