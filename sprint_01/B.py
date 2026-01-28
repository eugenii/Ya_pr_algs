# Чётные и нечётные числа

a, b, c = [int(i) for i in input().split()]

if a % 2 == b % 2 == c % 2:
    print("WIN")
else:
    print("FAIL")