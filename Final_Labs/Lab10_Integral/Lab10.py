"""
Беляев Никита, ИУ7-11б
Лабораторная работа №10. "Вычисление приближенного значения интеграла"

Задача:
1) Вычислить приближенное значение интеграла двумя методами
      Методы:
      1. Метод правых прямоугольников
      2. Метод трапеций
2) Рассчитать абсолютную и относительную погрешности для каждого из 4-х измерений
3) Определить наиболее точный метод
4) Итерационно вычислить, сколько разбиений нужно менее точному методу, чтобы вычислить интеграл
   с требуемой точностью
"""

import math as m


#    That code section contains functions for checking inputted  data
#    x_1, x_2 - boundaries of [x_1, x_2]. FLOAT
#    n_1, n_2 - amount of parts on [x_1,x_2]. +INT
#    eps - error for iterative integral calculation. +FLOAT


def get_boundaries():
    """ I check x_1 and x_2 """

    x_1 = input("Введите начальную границу отрезка интегрирования: ")
    x_2 = input("Введите конечную границу отрезка интегрирования: ")

    try:
        x_1, x_2 = float(x_1), float(x_2)
    except ValueError:
        print("\n(!) Границы интегрирования - это числа. Повторите ввод.")
        return None, None

    if x_1 == x_2:
        print("\n(!) Границы интегрирования совпадают. Интеграл равен 0. Повторите ввод.")
        return None, None

    if x_1 > x_2:
        x_1, x_2 = x_2, x_1
        global negative_check
        negative_check -= 1

    return x_1, x_2


def get_partitions():
    """ I check n_1 and n_2 """

    n_1 = input("Введите количество разбиений отрезка интегрирования для первого рассчета: ")
    n_2 = input("Введите количество разбиений отрезка интегрирования для второго рассчета: ")

    try:
        n_1, n_2 = float(n_1), float(n_2)
    except ValueError:
        print("\n(!) Количества разбиений - это положительные целые числа. Повторите ввод.")
        return None, None

    if int(n_1) != float(n_1) or int(n_2) != float(n_2) or n_1 <= 0 or n_2 <= 0:
        print("\n(!) Количества разбиений - это положительные целые числа. Повторите ввод.")
        return None, None

    return int(n_1), int(n_2)


def get_eps():
    """ I check error value """

    eps = input("Введите погрешность: ")
    try:
        eps = float(eps)
    except ValueError:
        print("\n(!) Погрешность - это положительное число. Повторите ввод.")
        return None

    if eps <= 0:
        print("\n(!) Погрешность - это положительное число. Повторите ввод.")
        return None
    return eps


#    This code section contains functions for calculating integral values & errors


def func(x):
    """I return function that User wants to integrate"""
    # m.sin(x)
    # x + 2
    # -(x ** 2)
    # x ** 2
    # x
    return x ** 2


def antiderivative(x):
    """ I return function's antiderivative"""
    # -(m.cos(x))
    # x ** 2 / 2 + 2 * x
    # -(x ** 3 / 3)
    # x ** 3 / 3
    # x ** 2 / 2
    return  x ** 3 / 3


def right_rect(func, interval, n):
    """I calculate the integral using Right Rectangle Method"""
    sum = 0
    dx = interval / n

    for i in range(1, n + 1, 1):
        sum += func(x_1 + i * dx) * dx

    return sum * (-1) ** negative_check


def trapeze(func, interval, n):
    """I calculate the integral using Trapeze Method"""
    sum = 0
    dx = interval / n

    for i in range(0, n, 1):
        sum += ((func(x_1 + i * dx) + func(x_1 + (i + 1) * dx)) * dx) / 2


    return sum * (-1) ** negative_check


def real_integral_value(x_1, x_2):
    """ I return precise integral value using function's antiderivative """
    return (antiderivative(x_2) - antiderivative(x_1)) * (-1) ** negative_check


def calculate_errors(method, parts, approximate_value):
    """ I calculate errors for each case and print it, return it """

    print(f"\n>> Погрешности метода {method} для {parts} разбиений(-я):")
    absolute_error = abs(approximate_value - integral)
    print("   Абсолютная: {:.5g}".format(absolute_error))

    if not bool(integral):
        print("   Точная величина интеграла равна 0. Относительная порешность не определена.")
        relative_error = None
    else:
        relative_error = abs(absolute_error * 100 / integral)
        print("Относительная: {:.5g}".format(relative_error))

    return absolute_error, relative_error


# Input section.
# If x_1 < x_2 integral value should be negative
# So we'll multiply it's value (Positive by default) on (-1) ** (negative_check - 1)
negative_check = 2
x_1, x_2 = None, None
n_1, n_2 = None, None

while x_1 is None and x_2 is None:
    x_1, x_2 = get_boundaries()

while n_1 is None and n_2 is None:
    n_1, n_2 = get_partitions()

interval = abs(x_2 - x_1)  # Length of [x_1, x_2]

# Calculating approximate integral values
rect_1 = right_rect(func, interval, n_1)
rect_2 = right_rect(func, interval, n_2)
trap_1 = trapeze(func, interval, n_1)
trap_2 = trapeze(func, interval, n_2)

# Outputting result's table
print("-" * 66)
print("|" + 30 * " " + "|{:^16.5g}|".format(n_1) + "{:^16.5g}|".format(n_2))
print("-" * 66)
print("|" + " Метод правых прямоугольников " + "|{:^16.5g}|".format(rect_1) + "{:^16.5g}|".format(rect_2))
print("-" * 66)
print("|" + " Метод трапеций " + 14 * " " + "|{:^16.5g}|".format(trap_1) + "{:^16.5g}|".format(trap_2))
print("-" * 66)

# Calculating Absolute (abs) and Relative (rel) errors for each case
integral = real_integral_value(x_1, x_2)
print(">> Истинное значение интеграла: {:.5g}".format(integral))

rect_abs_n1, rect_rel_n1 = calculate_errors("Правых прямоугольников", n_1, rect_1)
rect_abs_n2, rect_rel_n2 = calculate_errors("Правых прямоугольников", n_2, rect_2)
trap_abs_n1, trap_rel_n1 = calculate_errors("Трапеций", n_1, trap_1)
trap_abs_n2, trap_rel_n2 = calculate_errors("Трапеций", n_2, trap_2)

# Finding most precise method
most_precise = min(rect_abs_n1, rect_abs_n2, trap_abs_n1, trap_abs_n2)
name = ""  # Keeps the name of the MOST precise method
key = ""  # Keeps the name of the LEAST precise method

if most_precise == rect_abs_n1 or most_precise == rect_abs_n2:
    name = "Метод Правых Прямогульников"
    key = "Трапеций"
else:
    name = "Метод Трапеций"
    key = "Правых Прямоугольников"

print(f"\n{name} оказался наиболее точным.")

less_precise_method = {
    "Правых Прямоугольников": right_rect,
    "Трапеций": trapeze
}

# Calculating integral with inputted precision (EPS)
eps = None
while eps is None:
    eps = get_eps()

# Calculating amount of partitions we need to make in order to calculate integral with given precision
n = 1
while abs(less_precise_method[key](func, interval, n) - less_precise_method[key](func, interval, n * 2)) >= eps:
    n *= 2
print(f"C помощью метода {key} требуемой точности вычисления eps = {eps} удалось достигнуть за {n} разбиений(-я).")
print("Результат вычисления: {:.5g}".format(less_precise_method[key](func, interval, n)))
