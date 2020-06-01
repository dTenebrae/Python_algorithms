# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером
# 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме:
# по десять пар «код-символ» в каждой строке.


row_len = 10
start_sym = 32
MAX_SYM = 128

while start_sym < MAX_SYM:
    result = ''
    if MAX_SYM - start_sym < 10:
        row_len = MAX_SYM - start_sym
    for i in range(row_len):
        result += f'№{start_sym + i}: {chr(start_sym + i)} '
    start_sym += row_len
    print(result)

