# N Клумбы.

n = int(input())  # количество клумб
data = [[int(i) for i in input().split()] for _ in range(n)]

data.sort()    # отсортировали по левой границе

flowerbeds = [data[0]]

for flowerbed in data[1:]:
    if flowerbed[0] <= flowerbeds[-1][1]:
        flowerbeds[-1][1] = max(flowerbeds[-1][1], flowerbed[1])
    else:
        flowerbeds.append(flowerbed)

for _ in flowerbeds:
    print(_[0], _[1])
