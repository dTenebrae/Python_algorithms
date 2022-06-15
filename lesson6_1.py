# В диапазоне натуральных чисел от 2 до 99 определить, сколько из
# них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

import sys
from size import info_size

result = []
for i in range(2, 10):
    result.append((i, len([_ for _ in range(2, 100) if _ % i == 0])))
for item in result:
    print(f'{item[0]}: {item[1]}')

print(50 * '=')
print(sys.platform, sys.version)
print(50 * '=')
info_size(result, 'result')
print(50 * '=')
info_size(i, 'i')

# С использованием словаря
# ==================================================
# linux 3.8.2 (default, Apr 27 2020, 15:53:34)
# [GCC 9.3.0]
# ==================================================
# Имя, тип и размер объекта: result_dict, <class 'dict'>, 360 байт
# Объем информации в объекте: 128 байт
# Размер пустого объекта: 232 байт

# С использованием list'a
# ==================================================
# linux 3.8.2 (default, Apr 27 2020, 15:53:34)
# [GCC 9.3.0]
# ==================================================
# Имя, тип и размер объекта: result, <class 'list'>, 120 байт
# Объем информации в объекте: 64 байт
# Размер пустого объекта: 56 байт

# Выигрыш по памяти при использовании списка в три раза. С учетом размера входной информации и
# отсутствия необходимости быстрого доступа к элементам массива - использование
# хэш-таблицы нецелесообразно

