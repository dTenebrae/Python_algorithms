# Среди натуральных чисел, которые были введены, найти наибольшее по сумме
# цифр. Вывести на экран это число и сумму его цифр.


def num_sum(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result


x, y, z = map(int, input('Введите 3 числа через запятую: ').split(','))
if num_sum(z) <= num_sum(x) >= num_sum(y):
    print(f'Наибольшая сумма чисел {num_sum(x)} в числе {x}')
elif num_sum(x) <= num_sum(y) >= num_sum(z):
    print(f'Наибольшая сумма чисел {num_sum(y)} в числе {y}')
elif num_sum(x) <= num_sum(z) >= num_sum(y):
    print(f'Наибольшая сумма чисел {num_sum(z)} в числе {z}')
else:
    print('Something wrong...')
