# H sum of binaries

a, b = int(input()), int(input())

def b_sum(a, b):
    res = 0
    pos = 0
    r = 0
    m = max(a, b)
    n = min(a, b)
    while m > 0:
        res += ((m % 2 + n % 2 + r) % 2) * 10 ** pos
        r = (m % 2 + n % 2) // 2
        pos += 1
        m = m // 10
        n = n // 10
    return res + r * 10 ** pos


print(b_sum(a, b))
print(b_sum(1, 1))
print(b_sum(10, 11))
print(b_sum(1010, 1011))

# m, n = m ^ n, (m & n) << 1

# def b_sum(a, b):
#     res = 0
#     m = max(a, b)
#     n = min(a, b)
#     while n > 0:
#         res = m ^ n
#         n = (m & n) << 1
#     return m