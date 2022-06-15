# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.


from random import randint
from size import size_of, info_size
import sys

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

print(50 * '=')
print(sys.platform, sys.version)
print(50 * '=')
size_of(array)
print(50 * '=')
info_size(min_el)
print(50 * '=')
info_size(max_el)

# ==================================================
# linux 3.8.2 (default, Apr 27 2020, 15:53:34)
# [GCC 9.3.0]
# ==================================================
#  type = <class 'list'>, size = 256, object = [53, 2, 79, 66, 94, 32, 20, 39, 15, 34, 15, 64, 41,
#                                               96, 26, 64, 61, 78, 95, 46]
# 	 type = <class 'int'>, size = 28, object = 53
# 	 type = <class 'int'>, size = 28, object = 2
# 	 type = <class 'int'>, size = 28, object = 79
# 	 type = <class 'int'>, size = 28, object = 66
# 	 type = <class 'int'>, size = 28, object = 94
# 	 type = <class 'int'>, size = 28, object = 32
# 	 type = <class 'int'>, size = 28, object = 20
# 	 type = <class 'int'>, size = 28, object = 39
# 	 type = <class 'int'>, size = 28, object = 15
# 	 type = <class 'int'>, size = 28, object = 34
# 	 type = <class 'int'>, size = 28, object = 15
# 	 type = <class 'int'>, size = 28, object = 64
# 	 type = <class 'int'>, size = 28, object = 41
# 	 type = <class 'int'>, size = 28, object = 96
# 	 type = <class 'int'>, size = 28, object = 26
# 	 type = <class 'int'>, size = 28, object = 64
# 	 type = <class 'int'>, size = 28, object = 61
# 	 type = <class 'int'>, size = 28, object = 78
# 	 type = <class 'int'>, size = 28, object = 95
# 	 type = <class 'int'>, size = 28, object = 46
# ==================================================
# Имя, тип и размер объекта: unknown, <class 'list'>, 72 байт
# Объем информации в объекте: 16 байт
# Размер пустого объекта: 56 байт
# ==================================================
# Имя, тип и размер объекта: unknown, <class 'list'>, 72 байт
# Объем информации в объекте: 16 байт
# Размер пустого объекта: 56 байт

