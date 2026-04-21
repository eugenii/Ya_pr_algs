# D BFS
import sys
from queue import Queue

sys.setrecursionlimit(200000)

data = sys.stdin.read().split()

n = int(data[0])
m = int(data[1])

adj = [[] for _ in range(n + 1)]

cursor = 2
for i in range(m):
    u, v = int(data[cursor]), int(data[cursor + 1])
    adj[u].append(v)
    adj[v].append(u)
    cursor += 2

for _ in adj:
    _.sort()


s = int(data[cursor])

# print(n, m, adj, s, sep='\n')

color = ['white' for _ in range(n + 1)]
distance = [None for _ in range(n + 1)]
previous = [None for _ in range(n + 1)]

queue = Queue()
queue.put(s)
color[s] = 'gray'
distance[s] = 0
way = [s]

def bfs(s):
    planned = Queue()
    planned.put(s)
    color[s] = 'gray'
    distance[s] = 0

    while not planned.empty():
        u = planned.get()
        for v in adj[u]:
            if color[v] == 'white':
                color[v] = 'gray'
                distance[v] = distance[u] + 1
                previous[v] = u
                planned.put(v)
                way.append(v)
        color[u] = 'black'

bfs(s)
# print(*way)
print(max(distance[1:]))