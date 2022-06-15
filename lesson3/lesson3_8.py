# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов
# строк. Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.


matrix = [[0 for i in range(5)] for j in range(4)]

for j in range(4):
    sum_el = 0
    for i in range(5):
        if i == 4:
            matrix[j][i] = sum_el
        else:
            matrix[j][i] = int(input('Введите число: '))
            sum_el += matrix[j][i]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
