# G binary
# Перевод в двоичную систему

def binary(n):
    if n == 0:
        return 0
    return n % 2 + 10 * binary(n // 2)

print(binary(10))
print(binary(5))
print(binary(256))
print(binary(257))
print(binary(9))