import sys


def size_of(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                size_of(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                size_of(xx, level + 1)


def info_size(x, name='unknown'):
    print(f'Имя, тип и размер объекта: {name}, {type(x)}, {sys.getsizeof(x)} байт'
          f'\nОбъем информации в объекте: {sys.getsizeof(x) - sys.getsizeof(type(x)())} байт'
          f'\nРазмер пустого объекта: {sys.getsizeof(type(x)())} байт')
