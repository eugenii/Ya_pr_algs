# Ссылка на отчёт о решении:
# https://contest.yandex.ru/contest/22450/run-report/156206829/ 
import sys
import array


def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    res = array.array('I', [0] * n)
    
    inf = n + 1
    
    # Первый проход: слева направо
    dist = inf
    for i in range(n):
        
        if data[i + 1] == b'0':
            dist = 0
        else:
            dist += 1
        res[i] = dist
        
    # Второй проход: справа налево
    dist = inf
    for i in range(n - 1, -1, -1):
        if data[i + 1] == b'0':
            dist = 0
        else:
            dist += 1
        
        if dist < res[i]:
            res[i] = dist

    # Очистка данных (примерно 40 МБ)
    del data        
    sys.stdout.write(" ".join(map(str, res)) + "\n")

if __name__ == "__main__":
    solve()