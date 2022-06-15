# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.


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
array[min_el[1]], array[max_el[1]] = array[max_el[1]], array[min_el[1]]
print(array)