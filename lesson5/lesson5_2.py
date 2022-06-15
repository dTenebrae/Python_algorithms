# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры
# числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import defaultdict
from itertools import zip_longest

HEX_NUM = dict(zip('0123456789ABCDEF', range(16)))  # Тут поленился, сделал 2 словаря.
NUM_HEX = dict(zip(range(16), '0123456789ABCDEF'))  # Можно обойтись одним листом


def add_hex(first_hex, sec_hex):
    ovflw = 0
    result = []
    for i, j in zip_longest(first_hex[::-1], sec_hex[::-1], fillvalue='0'):
        result.append((HEX_NUM[i] + HEX_NUM[j] + ovflw) % 16)
        ovflw = 1 if (HEX_NUM[i] + HEX_NUM[j] + ovflw) > 15 else 0
    return ''.join([item for item in map(lambda x: NUM_HEX[x], result)][::-1])


def mult_hex(first_hex, sec_hex):
    ovflw = 0
    reg_count = 0
    part_lst = []

    if len(first_hex) <= len(sec_hex):  # Выбираем самое длинное число
        small = first_hex[::-1]         # и переворачиваем оба
        big = sec_hex[::-1]
    else:
        small = sec_hex[::-1]
        big = first_hex[::-1]

    for j in small:  # Создаем список для сложения со сдвигом регистра
        tmp = []
        for _ in range(reg_count):
            tmp.append(0)
        for i in big:
            tmp.append((HEX_NUM[i] * HEX_NUM[j] + ovflw) % 16)
            ovflw = (HEX_NUM[i] * HEX_NUM[j] + ovflw) // 16
        if ovflw:
            tmp.append(ovflw)
            ovflw = 0
        part_lst.append(tmp)
        reg_count += 1

    result = part_lst[0]  # Складываем в финальный результат
    tmp = []
    for k in range(1, len(part_lst)):
        for i, j in zip_longest(result, part_lst[k], fillvalue=0):
            tmp.append((i + j + ovflw) % 16)
            ovflw = 1 if (i + j + ovflw) > 15 else 0
        result = tmp.copy()
        tmp = []
    return ''.join([item for item in map(lambda x: NUM_HEX[x], result)][::-1])


hex_dict = defaultdict(list)
hex_dict['first'] += input('Введите первое число: ').upper()
hex_dict['second'] += input('Введите второе число: ').upper()

for i, j in zip_longest(hex_dict['first'], hex_dict['second'], fillvalue='0'):  # Проверка на
    if (i not in HEX_NUM.keys()) or (j not in HEX_NUM.keys()):                  # корректность ввода
        print('Некорректный ввод')
        exit(0)

sum_str = add_hex(hex_dict['first'], hex_dict['second'])
mult_str = mult_hex(hex_dict['first'], hex_dict['second'])
print(50 * '=')
print(f'Сложение: {sum_str}\nУмножение: {mult_str}')
print(50 * '=')
print('Встроенными функциями Python')
print('Сложение: ', hex(int(''.join(hex_dict['first']), 16) + int(''.join(hex_dict['second']), 16)))
print('Умножение: ',hex(int(''.join(hex_dict['first']), 16) * int(''.join(hex_dict['second']), 16)))
