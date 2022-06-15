# В одномерном массиве целых чисел определить два наименьших элемента. Они
# могут быть как равны между собой (оба минимальны), так и различаться.


from random import randint
import sys
from size import info_size

array = [randint(1, 100) for num in range(20)]
print(array)

min_els = [array[0], array[1]]
i = 2
while i < len(array):
    s = array[i]
    if array[i] < min_els[0]:
        min_els[0] = array[i]
    elif array[i] < min_els[1]:
        min_els[1] = array[i]
    i += 1

print(f'Минимальные элементы {min_els[0]} и {min_els[1]}')

print(50 * '=')
print(sys.platform, sys.version)
print(50 * '=')
info_size(min_els, 'min_els')
print(50 * '=')
info_size(array)
# С использованием 2х переменных типа int
# ==================================================
# linux 3.8.2 (default, Apr 27 2020, 15:53:34)
# [GCC 9.3.0]
# ==================================================
# Имя, тип и размер объекта: min1, <class 'int'>, 28 байт
# Объем информации в объекте: 4 байт
# Размер пустого объекта: 24 байт
# ==================================================
# Имя, тип и размер объекта: min2, <class 'int'>, 28 байт
# Объем информации в объекте: 4 байт
# Размер пустого объекта: 24 байт

# С использованием списка
# ==================================================
# linux 3.8.2 (default, Apr 27 2020, 15:53:34)
# [GCC 9.3.0]
# ==================================================
# Имя, тип и размер объекта: min_els, <class 'list'>, 72 байт
# Объем информации в объекте: 16 байт
# Размер пустого объекта: 56 байт

# Разница в объеме использованной памяти 16 байт