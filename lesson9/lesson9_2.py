# Закодируйте любую строку по алгоритму Хаффмана

# - Символы входного алфавита образуют список свободных узлов. Каждый лист имеет вес, который может
# быть равен либо вероятности, либо количеству вхождений символа в сжимаемое сообщение.

# - Выбираются два свободных узла дерева с наименьшими весами.

# - Создается их родитель с весом, равным их суммарному весу.

# - Родитель добавляется в список свободных узлов, а два его потомка удаляются из этого списка.

# - Одной дуге, выходящей из родителя, ставится в соответствие бит 1, другой — бит 0. Битовые
# значения ветвей, исходящих от корня, не зависят от весов потомков.

# - Шаги, начиная со второго, повторяются до тех пор, пока в списке свободных узлов не останется
# только один свободный узел. Он и будет считаться корнем дерева.

import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')  # Кодируем 0 если налево, 1 если направо
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'  # На случай пустой строки


def huffman(s: str) -> dict:
    h = []
    for ch, freq in Counter(s).items():  # Counter(s) Частота встречаемости freq
        h.append((freq, len(h), Leaf(ch)))  # символов ch в строке s. Символы пишем в листья
    heapq.heapify(h)  # Превращаем список в очередь с приоритетами
    count = len(h)
    while len(h) > 1:  # Пока не дошли до корня
        freq1, _count1, left = heapq.heappop(h)  # Берем пару самых редковстречающихся значений
        freq2, _count2, right = heapq.heappop(h)  # _count - мусорная переменная, чтобы при сравнении не вылетала ошибка
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # Суммируем частоту этих элементов и пишем в узел
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


s = input('Введите строку: ')
code = huffman(s)
encoded = ''.join(code[ch] for ch in s)
for ch in sorted(code):
    print(f'{ch}: {code[ch]}')
print(f'Число бит: {len(encoded)}\nЗакодированная строка: {encoded}')
