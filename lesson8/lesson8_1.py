# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько
# рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


try:
    N = int(input('Введите количество друзей: '))
except ValueError:
    print('Введены некорректные данные')

graph = [[1 if i != j else 0 for i in range(N)] for j in range(N)]  # Создаем граф с гранями до
for i, vertex in enumerate(graph):  # всех вершин, кроме самой себя
    print(i, vertex)

for i, vertex in enumerate(graph):
    for j, edge in enumerate(vertex):
        if edge:
            graph[j][i] = 0  # Обнуляем "рукопожатия" тех "друзей", с которыми уже "здоровались"

print(50 * '=')
sum_edges = 0
for i, vertex in enumerate(graph):
    print(i, vertex)
    sum_edges += sum(vertex)

print(f'Общее количество рукопожатий: {sum_edges}')
assert sum_edges == (N * (N - 1)) / 2, 'Некорректно'  # Проверка с формулой количества ребер графа
