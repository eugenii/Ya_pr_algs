# Решение задачи топологической сортировки
import sys

sys.setrecursionlimit(200000)

data = sys.stdin.read().split()
if not data:
    exit()

n = int(data[0])
m = int(data[1])

adj = [[] for _ in range(n + 1)]
color = ['white' for _ in range(n + 1)]
order = []

cursor = 2
for i in range(m):
    u = int(data[cursor])
    v = int(data[cursor + 1])  # cursor += 2; cursor = 2*i+2; cursor = 2*i+3; cursor = 2*(i+1) = 
    adj[u].append(v)
    cursor += 2
for _ in adj:
    _.sort()

print(adj)

def top_sort(v):
    color[v] = 'gray'
    for neighbour in adj[v]:
        if color[neighbour] == 'white':
            top_sort(neighbour)
    color[v] = 'black'
    order.append(v)


def main_top_sort():
    for v in range(1, n + 1):
        if color[v] == 'white':
            top_sort(v)
    result = [str(i) for i in order[::-1]]
    print(' '.join(result))


main_top_sort()