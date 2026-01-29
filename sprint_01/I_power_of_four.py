# I Степень четырёх.
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0


def isPowerOfFour(n):
    if n == 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return isPowerOfFour(n // 4)
    return False

print(isPowerOfFour(int(input())))