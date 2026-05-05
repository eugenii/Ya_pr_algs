# Слабое звено.
import sys

# 1. Лимит рекурсии (важно!)
sys.setrecursionlimit(100000)

data = sys.stdin.read().split()

n, m = int(data[0]), int(data[1])

adj = [[] for I in range(n + 1)]
colors = ['white' for _ in range(n + 1)]

cursor = 2
for _ in range(m):
    u, v = int(data[cursor]), int(data[cursor + 1])
    adj[u].append(v)
    cursor += 2

cycle = [0]

def DFS(v):
    colors[v] = 'gray'
    for w in adj[v]:
        if colors[w] == 'gray':
            cycle[0] = 1
        if colors[w] == 'white':
            DFS(w)
    colors[v] = 'black'


def main_dfs():
    for vert in range(1, n + 1):
        if colors[vert] == 'white':
            DFS(vert)


main_dfs()

print('YES' if cycle[0] == 1 else 'NO')

# тестовые данные
# 4 5
# 1 2
# 1 3
# 2 3
# 3 1
# 4 1