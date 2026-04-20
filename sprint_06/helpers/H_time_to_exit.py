# Решение задачи Н Время выходить.
import sys
sys.setrecursionlimit(300000)


data = sys.stdin.read().split()
n = int(data[0])
m = int(data[1])

visited = [False] * (n + 1)
adj = [[] for _ in range(n + 1)]
tin = [0] * (n + 1)
tout = [0] * (n + 1)

cursor = 2
for _ in range(m):
    u = int(data[cursor])
    v = int(data[cursor + 1])
    adj[u].append(v)
    cursor += 2

for neighbors in adj:
    neighbors.sort()

timer = [0] # Используем список, чтобы менять его внутри функции


def dfs(v):
    
    # 1. Записываем время входа для v
    visited[v] = True
    tin[v] = timer[0]
    timer[0] += 1
    for neighbour in adj[v]:
        
        dfs(neighbour)
    tout[v] = timer[0]
    timer[0] += 1

dfs(1)
# Сборка вывода
output = []
for v in range(1, n + 1):
    output.append(f'{tin[v]} {tout[v]}')

sys.stdout.write("\n".join(output))
# print(adj, tin, tout, visited)