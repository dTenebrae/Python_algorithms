# Пользователь вводит данные о количестве предприятий, их наименования и
# прибыль за четыре квартала для каждого предприятия. Программа должна
# определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import defaultdict

# vars
firm_num = 0
sum_f = 0
f_dict = dict()
res_dict = defaultdict(list)
tmp_list = []

try:
    firm_num = int(input('Введите количество предприятий: '))
except ValueError:
    print('Необходимо ввести целое число')
    exit(0)
if firm_num <= 0:
    exit(0)
for i in range(firm_num):
    tmp_list = input(f'Введите название предприятия {i + 1} '
                     f'и его прибыль за 4 квартала: ').split()
    try:
        f_dict[tmp_list[0]] = int(tmp_list[1])
        sum_f += int(tmp_list[1])
    except:
        print('Ошибка ввода')
        exit(0)

for key in f_dict.keys():
    if f_dict[key] >= sum_f / firm_num:
        res_dict['More'].append(key)
    else:
        res_dict['Less'].append(key)

print(f'\nПри средней прибыли за год {sum_f / firm_num}, '
      f'предприятия с выручкой \nвыше среднего:')
for value in res_dict['More']:
    print(value, end=' ')
print('\nНиже: ')
for value in res_dict['Less']:
    print(value, end=' ')
