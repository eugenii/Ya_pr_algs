import sys

# 1. увеличиваем лимит рекурсии
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n + 1)]
    
    # 2. чтение ребер
    cursor = 2
    for _ in range(m):
        u = int(data[cursor])
        v = int(data[cursor + 1])
        adj[u].append(v)
        adj[v].append(u) # Граф неориентированный
        cursor += 2

    color = [-1] * (n + 1)
    components = []


    def dfs(v, current_component):
        color[v] = 1
        current_component.append(v)
        for neighbor in adj[v]:
            if color[neighbor] == -1:
                dfs(neighbor, current_component)

    for i in range(1, n + 1):
        if color[i] == -1:
            current_component = []
            dfs(i, current_component) 
            components.append(current_component)

    # Вывод результата
    print(len(components))
    for comp in components:
        comp.sort()
        # Выводим количество вершин в компоненте
        print(len(comp))
        # Выводим сами вершины через пробел
        print(*(comp))

if __name__ == '__main__':
    solve()
