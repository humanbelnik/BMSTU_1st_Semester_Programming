'''
Беляев Никита, ИУ-711б
Лабораторная работа №4

Задание:
Построить таблицу значений функции и построить график.
Функция: y = x**8 - 5*x**7 + 3*x**6 + 8*x**5 - 35*x**4 + 73*x**3 - 6*x**2 + 23*x + 7
'''

# Входные данные и константы
import math as m

x_first = float(input('Введите начальное значение аргумента: '))
x_last = float(input('Введите конечное значение аргумента: '))
step = float(input('Введите шаг аргумента: '))

WIDTH = 80  # Фиксированная ширина графика
eps = (1/2) * step  # Погрешность
check_if_zero = False

y_max = float('-inf')
y_min = float('inf')

# Построение таблицы значений функции
print('|' + '-' * 27 + '|')
print('|{: ^13}|{: ^13}|'.format('x', 'y'))
print('|' + '-' * 27 + '|')

x = x_first
while x <= x_last + eps:
    y_current = x**8 - 5*x**7 + 3*x**6 + 8*x**5 - 35*x**4 + 73*x**3 - 6*x**2 + 23*x + 7
    if y_current > y_max:
        y_max = y_current
    if y_current < y_min:
        y_min = y_current
    print('|{: ^13.3f}|{: ^13.5}|'.format(x, y_current))
    x += step
delta = y_max - y_min  # Длина локальной области значений

print('|' + '-' * 27 + '|')
print('|{: ^27}|'.format('y_max - y_min'))
print('|' + '-' * 27 + '|')
print('|{: ^27.5}|'.format(delta))
print('|' + '-' * 27 + '|')

# Разметка оси "Y" и ее построение
y_marks = int(input('Введите количество засечек по оси Y в кол-ве от 4-х до 8-ми: '))
symb = int(WIDTH/y_marks)  # Количество символов, отведенное под отсчеку
space = ' ' * 8

y_step = delta/(y_marks - 1)  # Численная разность между двумя отсчеками
y_mark_current = y_min
i = 1
while i <= y_marks:
    if i == 1:
        space += f"{y_mark_current:<{symb}g}"
    elif i < y_marks:
        space += f"{y_mark_current:^{symb}g}"
    else:
        space += f"{y_mark_current:>{symb}g}"
    i += 1
    y_mark_current += y_step
print(space)
print(' ' * 6 + '-' * 83 + '>')

# Построение графика:


index = (y_max - y_min)/WIDTH  # Индекс масштабирования
zero_idx = None  # Хранит в себе позицию ОХ
if y_min <= 0 <= y_max:  # Проверяем, пересекает ли ОХ
    zero_idx = int(-y_min /index)

while x_first <= x_last + step:
    y = (x_first)**8 - 5*(x_first)**7 + 3*(x_first)**6 + 8*(x_first)**5 - 35*(x_first)**4 + 73*(x_first)**3 - 6*(x_first)**2 + 23*(x_first) + 7
    position = int((y - y_min) / index)  # позиция значения функции на области печати графика

    if zero_idx is not None:  # проверка на пересечение оси абсцисс на заданном отрезке
        if position < zero_idx:  # если точка лежит ниже оси абсцисс
            line = " " * position + "*" + " " * (zero_idx - position - 1) + "|"
        elif position == zero_idx:  # если точка лежит на оси абсцисс
            line = " " * position + "*"
        else:  # если точка лежит выше оси абсцисс
            line = " " * zero_idx + "|" + " " * (position - zero_idx - 1) + "*"
    else:  # если график не пересекает ось абсцисс
        line = " " * position + "*"
    print(f"{round(x_first,6):>6g}|" + line)
    x_first += step

























