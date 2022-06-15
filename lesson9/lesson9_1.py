# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции
# дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля
# hashlib задача считается не решённой.


from hashlib import sha1


def sub_str(some: str):
    some_trimmed = some.replace(' ', '')  # Убираем из строки пробелы
    whole_str_trm = sha1(some_trimmed.encode('utf-8')).hexdigest()  # Создаем хэш полной строки
    for i, letter in enumerate(some_trimmed):
        j = i + 1
        while j <= len(some_trimmed):
            counter = 0
            tmp_str = some_trimmed[i:j]  # Берем подстроку
            tmp_hash = sha1(tmp_str.encode('utf-8')).hexdigest()  # Вычисляем ее хэш
            if tmp_hash != whole_str_trm:  # Проверяем, не равен ли он хэшу полной строки
                for k in range(
                        len(some_trimmed) - len(tmp_str) + 1):  # Используем алгоритм Карпа-Рабина
                    if tmp_hash == sha1(
                            some_trimmed[k:k + len(tmp_str)].encode('utf-8')).hexdigest():
                        counter += 1
                print(f'{tmp_str} = {counter}')
            j += 1


while True:
    string = input('Введите строку: ')
    if string:
        break
sub_str(string)
