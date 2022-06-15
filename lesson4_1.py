# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

from random import randint
# import cProfile

def double_cycle(n):
    array = [randint(1, 100) for _ in range(n)]
    min_var = max_var = array[0]
    for item in array:
        if item < min_var:
            min_var = item
    for item in array:
        if item > max_var:
            max_var = item
    array[array.index(min_var)], array[array.index(max_var)] = \
        array[array.index(max_var)], array[array.index(min_var)]
# double_cycle(100)
# 537 function calls in 0.000 seconds
# double_cycle(1000)
# 5289 function calls in 0.002 seconds
# double_cycle(1000000)
# 5278999 function calls in 1.533 seconds
# double_cycle(10000000)
# 52800263 function calls in 15.048 seconds

# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.double_cycle(100)"
# 1000 loops, best of 5: 70.4 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.double_cycle(1000)"
# 1000 loops, best of 5: 685 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.double_cycle(10000)"
# 1000 loops, best of 5: 6.92 msec per loop

def min_max(n):
    array = [randint(1, 100) for _ in range(n)]
    min_el = [array[0], 0]
    max_el = [array[0], 0]
    for i, item in enumerate(array):
        if min_el[0] > item:
            min_el[0], min_el[1] = item, i
        if max_el[0] < item:
            max_el[0], max_el[1] = item, i
    array[min_el[1]], array[max_el[1]] = array[max_el[1]], array[min_el[1]]
# min_max(100)
# 536 function calls in 0.000 seconds
# min_max(1000)
# 5267 function calls in 0.003 seconds
# min_max(1000000)
# 5279677 function calls in 1.570 seconds
# min_max(10000000)
# 52798600 function calls in 15.440 seconds
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.min_max(100)"
# 1000 loops, best of 5: 72.2 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.min_max(1000)"
# 1000 loops, best of 5: 727 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.min_max(10000)"
# 1000 loops, best of 5: 7.27 msec per loop

def min_max_py(n):
    array = [randint(1, 100) for _ in range(n)]
    array[array.index(min(array))], array[array.index(max(array))] = \
        array[array.index(max(array))], array[array.index(min(array))]
# min_max_py(100)
# 545 function calls in 0.000 seconds
# min_max_py(1000)
# 5339 function calls in 0.002 seconds
# min_max_py(1000000)
# 5280485 function calls in 1.539 seconds
# min_max_py(10000000)
# 52799604 function calls in 15.133 seconds
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.min_max_py(100)"
# 1000 loops, best of 5: 70.7 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.min_max_py(1000)"
# 1000 loops, best of 5: 702 usec per loop
# python3 -m timeit -n 1000 -s "import lesson4_1" "lesson4_1.min_max_py(10000)"
# 1000 loops, best of 5: 6.97 msec per loop

def main():
    pass
    # double_cycle(10000000)
    # # min_max(10000000)
    # # min_max_py(10000000)

# cProfile.run('main()')





