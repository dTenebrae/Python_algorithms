# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.


from random import randint

array = [randint(1, 100) for num in range(20)]
print(array)

min_el = [array[0], 0]
max_el = [array[0], 0]
for i, item in enumerate(array):
    if min_el[0] > item:
        min_el[0], min_el[1] = item, i
    if max_el[0] < item:
        max_el[0], max_el[1] = item, i
i = min_el[1] + 1 if min_el[1] < max_el[1] else max_el[1] + 1
j = max_el[1] - 1 if min_el[1] < max_el[1] else min_el[1] - 1
sum_el = 0
while i <= j:
    sum_el += array[i]
    i += 1
print(f'Минимальный элемент {min_el[0]} расположен на позиции {min_el[1]}\n'
      f'Максимальный элемент {max_el[0]} расположен на позиции {max_el[1]}\n'
      f'Сумма элементов между ними {sum_el}')
