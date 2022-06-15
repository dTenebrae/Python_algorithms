# Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором
# все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


from random import randint, choice


def graph_gen(n):
    """Генерация графа происходит следующим образом:
    в вершину графа помещаем лист случайных чисел от 0 до общего количества вершин(n),
    за исключением случаев, когда она ссылается сама на себя (убираем петли). Кроме того,
    количество ребер делаем случайным в пределах от 1(ноль убираем, чтобы не было
    изолированных вершин. Правда это убирает и вершины, в которые приходит
    ребро, но из которых ничего не уходит) до n. И так n раз"""
    return [list(set([choice([i for i in range(0, n) if i != j])
                      for _ in range(randint(1, n - 1))])) for j in range(n)]


result = []


def dfs(vertex, graph, visited):
    visited[vertex] = True
    for edge in graph[vertex]:
        if not visited[edge]:
            visited[edge] = True
            result.append(edge)
            return dfs(edge, graph, visited)


try:
    N = int(input('Введите число вершин графа: '))
    start = int(input(f'Введите стартовую вершину от 0 до {N - 1}: '))
except ValueError:
    print('Некорректный ввод')
    exit(0)

if N <= 1 or start >= N:
    print('Некорректный ввод')
    exit(0)

graph1 = graph_gen(N)
is_visited = [False for _ in graph1]
for i, item in enumerate(graph1):
    print(f'Вершина {i} -> {item}')

dfs(start, graph1, is_visited)
print(f'Из точки {start} путь проходит через {"->".join(map(str, result))}')
