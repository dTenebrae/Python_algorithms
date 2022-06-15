# Найти максимальный элемент среди минимальных элементов столбцов матрицы


from random import randint

ROW = 10
COLUMN = 10
matrix = [[randint(1, 50) for i in range(ROW)] for j in range(COLUMN)]
min_els = [0 for _ in range(COLUMN)]
# Красиво печатаем матрицу
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
# Ищем минимальные элементы по столбцам
for i in range(COLUMN):
    min_els[i] = matrix[0][i]
    for j in range(ROW):
        if matrix[j][i] < min_els[i]:
            min_els[i] = matrix[j][i]
# Ищем максимальный элемент среди минимальных
max_el = min_els[0]
for item in min_els:
    if max_el < item:
        max_el = item
# Некрасиво печатаем результат
print('\n', '-' * 40)
for item in min_els:
    print(f'{item:>4}', end='')
print(f'\n\nМаксимальное значение: {max_el}')
