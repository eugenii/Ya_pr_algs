# A Список смежности.

vertices, edges = map(int, input().split())

incident_list = [[] for _ in range(vertices + 1)]

for _ in range(edges):
    u, v = map(int, input().split())
    incident_list[u].append(v)
incident_list.pop(0)

for i in incident_list:
    print(len(i), *i)

# print(incident_list)

# for _ in range(edges):
#     v1, v2 = map(int, input().split())
#     incident_list[v1].append(v2)
#     incident_list[v2].append(v1)

# for i in range(vertices):
#     print(len(incident_list[i]), *sorted(incident_list[i])) 