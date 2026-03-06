# E Покупка домов.

"""
Подсчёт количества домов, которые можно купить.
"""

def main(arr:list[int], budget:int) -> int:
    rest = budget
    count = 0
    for i in arr:
        if i <= rest:
            count += 1
            rest -= i
            continue
        break
    return count
        
        
n, budget = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(main(arr, budget))