# H binary sum 2 (strings)

# a, b = input(), input()


def b_sum(a, b):
    a, b = max(a, b, key=lambda x: (len(x), x)), min(a, b, key=len)
    # a_r = a[len(a) - len(b) - 1 :]
    r = 0
    res = ''
    for i in range(-1, -len(a) - 1, -1):
        if abs(i) <= len(b):
            # res = a[i] + res
            if a[i] == b[i] == '0':
                res = str(r) + res
                r = 0
            if a[i] == b[i] == '1':
                res = str(r) + res
                r = 1
            if a[i] == '0' and b[i] == '1':
                if r == 1:
                    res = '0' + res 
                    r = 1
                else:
                    res = '1' + res
                    r = 0
            if a[i] == '1' and b[i] == '0':
                if r == 1:
                    res = '0' + res 
                    r = 1
                else:
                    res = '1' + res
                    r = 0
        else:
            if a[i] == '1' and r == 1:
                res = '0' + res
                r = 1
            elif a[i] == '1' and r == 0:
                res = '1' + res
                r = 0
            else:
                res = str(r) + res
                r = 0
    if r == 1:
        res = str(r) + res
    return res

# print(b_sum(a, b))
print(b_sum('100', '0'))
# print(b_sum('10', '11'))
# print(b_sum('1010', '1011'))
# print(b_sum('111', '1'))