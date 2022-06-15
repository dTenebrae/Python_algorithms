# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка
# пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


from random import randint


def bubble_sort(array):
    n = 1
    change_flag = True  # Добавил флаг изменения в массиве для исключения прохождения по уже
    while n < len(array) and change_flag:  # отсортированному
        change_flag = False
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                change_flag = True
        n += 1


arr = [randint(-100, 100) for _ in range(30)]
print(arr)
bubble_sort(arr)
print(arr)
