'''
Беляев Никита, ИУ7-11б
Лабораторная работа №5 "Вычисление суммы бесконечного ряда"

Описание:
Вычилить сумму ряда: y = 1 + x/1! + x^2/2! + ... + x^n/n! (y = S(x^n/n!) n от 0)c заданной точность Epsilon.
Вывести таблицу промежуточных значений с заданным шагом
'''
# Приветствие
print('Данная программа вычисляет сумму ряда Y = SUM(x^n/n!) где n >= 0.')
# Блок ввода
x = float(input('Введите значение аргумента: '))
EPS = float(input('Введите значение точности (Положительное число): '))
iterations_max = int(input('Введите максимальное количество итераций (Положительное целое число): '))
print_step = int(input('Введите шаг печати (Положительное целое число): '))

# Необходимые величины
# n - порядковы номер слагаемого, cur - текущее слагаемое, sum - сумма ряда
n = 0
cur = 1
sum = 0
check = True
TABLE_WIDTH = 59

# Печать заголовка таблицы
print('|' + '-' * (TABLE_WIDTH - 2) + '|')
print('|{: ^17}|{: ^19}|{: ^19}|'.format('№ Итерации', 'T', 'S'))
print('|' + '-' * (TABLE_WIDTH - 2) + '|')

# Вычисление суммы
while abs(cur) >= EPS:
    sum += cur
    # Печать таблицы с заданным шагом
    if n % print_step == 0:
        print('|{: ^17}|{: <19.9g}|{: <19.9g}|'.format(n + 1, cur, sum))
    #  Вычисление следующего слагаемого в сумме и увеличение счетчика
    cur *= x/(n + 1)
    n += 1

    # Проверка, превысило ли текущее количество слагаемых заданное максимальное
    if n >= iterations_max:
        check = False
        break

# Печать результата
print('|' + '-' * (TABLE_WIDTH - 2) + '|')
if check:
    print('Сумма {:g} вычислена за {} итераций(-ии)'.format(sum, n))
else:
    print('Требуемой точности не удалось достигнуть за {} итераций(-ию)'.format(iterations_max))



















