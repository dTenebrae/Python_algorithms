# Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список
# вершин, которые необходимо обойти.


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost, parent


def path_rec(ent_point, parents):
    if parents[ent_point] == -1:
        print(ent_point)
        return
    print(ent_point, end=' <> ')
    path_rec(parents[ent_point], parents)

graph1 = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]
s = int(input('start: '))
result = dijkstra(graph1, s)
for i in range(len(result[1])):
    if result[0][i] == float('inf'):
        print(f'Вершина {i}: из вершины {s} недоступна')
    elif i == s:
        print(f'Вершина {i}: Вы стартовали отсюда')
    else:
        print(f'Вершина {i}, длина пути {result[0][i]}, путь: ', end='')
        path_rec(i, result[1])
