# A Биржа
import sys

days = int(input())
prices = list(map(int, input().split()))
profit = 0    # Прибыль

for idx in range(len(prices) - 1):
    if prices[idx + 1] > prices[idx]:
            profit += prices[idx + 1] - prices[idx]

print(profit)
