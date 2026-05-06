# A Биржа
import sys

days = int(input())
prices = list(map(int, input().split()))
acc = 0    # Стоимость акции на руках
profit = 0    # Прибыль

for idx in range(len(prices) - 1):
    if acc == 0:
        if prices[idx + 1] > prices[idx]:
            acc = prices[idx]
            continue
    if acc:
        if prices[idx + 1] < prices[idx]:
            profit += prices[idx] - acc
            acc = 0
            continue
if acc:
    profit += prices[idx + 1] - acc

print(profit)
