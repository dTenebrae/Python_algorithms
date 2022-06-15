# В диапазоне натуральных чисел от 2 до 99 определить, сколько из
# них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

result_dict = dict()
for i in range(2, 10):
    result_dict[i] = [num for num in range(2, 100) if num % i == 0]
for key in result_dict.keys():
    print(f'{key}: {result_dict[key]}')
