# В одномерном массиве целых чисел определить два наименьших элемента. Они
# могут быть как равны между собой (оба минимальны), так и различаться.


from random import randint


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