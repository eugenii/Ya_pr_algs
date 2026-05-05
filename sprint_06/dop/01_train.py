import sys

# 1. Читаем данные
data = sys.stdin.read().split()
if not data: exit()

n, m = int(data[0]), int(data[1])
k = int(data[-1])

# 2. Строим граф
adj = [[] for _ in range(n + 1)]
cursor = 2
for _ in range(m):
    u, v = int(data[cursor]), int(data[cursor + 1])
    adj[u].append(v)
    adj[v].append(u)
    cursor += 2

# 3. Итеративный DFS
stack = [1]
visited = [False] * (n + 1)
visited[1] = True # Помечаем корень сразу

# Если Алексей и есть Мария (k=1)
if k == 1:
    print("YES")
    sys.exit()

found = False
while stack:
    curr = stack.pop()
    
    for neighbor in adj[curr]:
        if neighbor == k:
            found = True
            break # Выход из for
        
        if not visited[neighbor]:
            visited[neighbor] = True # Помечаем ПЕРЕД добавлением
            stack.append(neighbor)
            
    if found: break # Выход из while

# 4. Результат
print("YES" if found else "NO")
