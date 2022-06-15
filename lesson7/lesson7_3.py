# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве
# медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся
# элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также
# недопустима).


import random
from statistics import median  # Встроенная функция нахождения медианы


def select_nth(n, items):
    pivot = random.choice(items)  # Выбираем опорный элемент

    lesser = [item for item in items if item < pivot]  # Создаем массив элементов меньше опорного
    if len(lesser) > n:  # Если он получился больше половины
        return select_nth(n, lesser)  # Рекурсивно идем в него, так как медиана в нем
    n -= len(lesser)  # Иначе уменьшаем n (бывшее число - половина массива) на длину этого массива

    numequal = items.count(pivot)  # Считаем количество чисел, равных опорному
    if numequal > n:  # Если их больше n
        return pivot  # Возвращаем опорный
    n -= numequal  # Иначе цменьшаем n на количество опорных

    greater = [item for item in items if item > pivot]  # Создаем массив элементов больше опорного
    return select_nth(n, greater)  # Рекурсивно идем в него


def median_alg(items):
    if len(items) % 2:  # Если длина массива нечетная
        return select_nth(len(items) // 2, items)  # делим его пополам нацело

    else:  # Этот случай у нас никогда не сработает, потому что длина массива всегда нечетная
        left = select_nth((len(items) - 1) // 2, items)
        right = select_nth((len(items) + 1) // 2, items)
        return (left + right) / 2


M = 15
arr = [random.randint(0, 20) for _ in range(2 * M + 1)]
print(arr)
print(median_alg(arr))
print(median(arr))  # Проверяем встроенной функцией
