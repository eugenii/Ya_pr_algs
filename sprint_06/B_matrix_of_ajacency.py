# B Матрица смежности

vertices, edges = map(int, input().split())
edges_list = [[] for _ in range(vertices)]

for edge in range(edges):
    u, v = map(int, input().split())
    edges_list[u - 1].append(v)
# edges_list.pop(0)
# print(edges_list)

matrix_of_ajacency = [[0] * (vertices) for _ in range(vertices)]
for row in range(vertices):
    for col in range(vertices):
        if col + 1 in edges_list[row]:
            matrix_of_ajacency[row][col] = 1

for row in range(vertices):
    print(*matrix_of_ajacency[row])


# print(*matrix_of_ajacency, sep='\n')