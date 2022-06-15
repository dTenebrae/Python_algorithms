# Определить, какое число в массиве встречается чаще всего


from random import randint


array = [randint(1, 7) for num in range(20)]
print(array)
max_item = [0, 0]
for num in set(array):
    if max_item[1] < array.count(num):
        max_item = [num, array.count(num)]
print(f'Число {max_item[0]} встречается {max_item[1]} раз')
