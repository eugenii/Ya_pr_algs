# Ближайший ноль.

# buldings
n = int(input())
street = [int(i) for i in input().split()]

# zeros
zeros = [i for i in range(n) if street[i] == 0]

def fill(left, right):
    res = '' 
    dist = right - left - 1
    r = 0
    if dist % 2 == 0:
        for i in range(dist // 2):
            r += 1
            res += str(r) + ' '
        for i in range(dist // 2):
            res += str(r) + ' '
            r -= 1
    else:
        for i in range(dist // 2 + 1):
            r += 1
            res += str(r) + ' '
        for i in range(dist // 2):
            r -= 1
            res += str(r) + ' '
            # r -= 1
    return res


def fill_start(pos):
    res = ''
    for i in range(pos):
        res += str(pos - i) + " "
    return res


def fill_end(pos, end):
    res = ''
    for i in range(1, end - pos):
        res += str(i) + ' '
    return res

def solution(street, zeros):
    if len(zeros) == 1:
        if zeros[0] == 0:
            return "0 " + fill_end(zeros[0], len(street))
        elif zeros[0] == len(street) - 1: 
            return fill_start(zeros[0]) + "0" 
        return fill_start(zeros[0]) + "0 " + fill_end(zeros[0], len(street))

# print(street, zeros)
print(solution(street, zeros))
# print(fill(2, 13))
# print(fill_start(5))
# print(fill_start(1))
# print(fill_start(0))
# print(fill_end(3, 9))

# for i in range(n):
#     if street[i] == 1:
#         print(min(abs(i - zeros[0]), abs(i - zeros[-1])))