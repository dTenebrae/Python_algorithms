# В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и
# «максимальный отрицательный». Это два абсолютно разных значения.


from random import randint

array = [randint(-50, 10) for num in range(20)]
print(array)
min_el = [-1, 0]
for i, num in enumerate(array):
    if num < 0 and min_el[0] == -1:
        min_el[0], min_el[1] = i, num
    elif min_el[1] < num < 0:
        min_el[0], min_el[1] = i, num

print(f'Число {min_el[1]} на позиции {min_el[0]}')
