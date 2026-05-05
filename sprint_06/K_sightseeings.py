import sys
import heapq

class Graph:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj

    def dijkstra(self, start_node):
        distances = [float('inf')] * (self.n + 1)
        distances[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > distances[u]:
                continue
                
            for v, weight in self.adj[u]:
                if distances[v] > distances[u] + weight:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))
        return distances

def solve():
    data = sys.stdin.read().split()
    if not data: return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    cursor = 2
    for _ in range(m):
        u = int(data[cursor])
        v = int(data[cursor + 1])
        w = int(data[cursor + 2])
        adj[u].append((v, w))
        adj[v].append((u, w)) # Мосты двусторонние
        cursor += 3
        
    graph = Graph(n, adj)
    
    # Генерируем матрицу
    for i in range(1, n + 1):
        res = graph.dijkstra(i)
        # Обработка строки для вывода
        formatted_row = []
        for dist in res[1:]:
            formatted_row.append(str(dist) if dist != float('inf') else "-1")
        print(" ".join(formatted_row))

solve()
