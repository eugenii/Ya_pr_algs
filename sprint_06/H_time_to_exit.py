import sys

sys.setrecursionlimit(400000)

def solve():
    # Быстрое чтение
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    cursor = 2
    for _ in range(m):
        u = int(input_data[cursor])
        v = int(input_data[cursor+1])
        adj[u].append(v)
        cursor += 2
    
    # Сортировка соседей по возрастанию
    for neighbors in adj:
        neighbors.sort()
    
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    visited = [False] * (n + 1)
    timer = [0]

    def dfs(v):
        visited[v] = True
        tin[v] = timer[0]
        timer[0] += 1
        
        for neighbor in adj[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        
        tout[v] = timer[0]
        timer[0] += 1

    # Запускаем от вершины 1 по условию
    dfs(1)
    
    # Формируем вывод
    output = []
    for i in range(1, n + 1):
        output.append(f"{tin[i]} {tout[i]}")
    
    sys.stdout.write("\n".join(output) + "\n")

solve()