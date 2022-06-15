# Написать программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое
# натуральное число.


# Циклом
def f_cycle(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Рекурсией
def f_rec(n):
    if n != 0:
        return n + f_rec(n - 1)
    else:
        return n


def eq_func(n):
    return int(n * (n + 1) / 2)


num = int(input('Введите число n: '))
print(f'Выражения 1+2+...+n = {f_rec(num)},  n(n+1)/2 = {eq_func(num)}. '
      f'Следовательно, равенство выполняется')
