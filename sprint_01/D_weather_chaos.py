# D. Weather chaos
n = int(input())
data = [int(i) for i in input().split()]

def solution(data):
    result = 0
    # базовые случаи
    if len(data) == 1:
        return 1
    if len(data) == 2:
        if data[1]!= data[0]:
            return 1
        else:
            return 0
    # остальные случаи
    if data[0] > data[1]:
        result += 1
    if data[-1] > data[-2]:
        result += 1
    for day in range(1, len(data) - 1):
        if data[day] > data[day - 1] and data[day] > data[day + 1]:
            result += 1
    return result
    

print(solution(data))