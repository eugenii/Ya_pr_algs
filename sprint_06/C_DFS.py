# C. DFS
import sys

sys.setrecursionlimit(200000)

def dfs(v, graph):
    """Обход графа в глубину."""
    visited[v] = True
    print(v, end=' ')
    for neighbour in graph[v]:
        if not visited[neighbour]:
            dfs(neighbour, graph)


data = sys.stdin.read().split()
if not data:
    exit()
n, m = map(int, data[:2])

adj = [[] for _ in range(n + 1)]

cursor = 2
for edge in range(m):
    u = int(data[cursor])
    v = int(data[cursor + 1])
    adj[u].append(v)
    adj[v].append(u)
    cursor += 2
s = int(data[cursor]) 

for neighbours in adj:
    neighbours.sort()

visited = [False] * (n + 1)

dfs(s, adj)