# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой
# треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.


a = int(input('Введите 1-ю сторону треугольника: '))
b = int(input('Введите 2-ю сторону треугольника: '))
c = int(input('Введите 3-ю сторону треугольника: '))

if a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')
