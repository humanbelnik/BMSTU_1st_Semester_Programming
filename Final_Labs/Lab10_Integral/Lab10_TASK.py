"""
Защита:
Посчитать интеграл f = x ** 2 методом срединных прямоугольников с заданной точностью
"""


def get_boundaries():
    """ Checking inputs """

    x_1 = float(input("Введите начало отрезка: "))
    x_2 = float(input("Введите конец отрезка: "))

    if x_1 == x_2:
        print("Границы отрезка интегрирования совпадают. Интеграл равен 0.")
        return None, None
    if x_1 > x_2:
        x_1, x_2 = x_2, x_1
        global reversed_check
        reversed_check = 1
    return x_1, x_2


def func(x):
    """ I return function """
    return x ** 2


def antiderivative(x):
    return x ** 3 / 3


def true_integral_value():
    return (antiderivative(x_2) - antiderivative(x_1)) * (-1) ** reversed_check


def middle_rectangle_method(func, interval, n):
    """ Calculating integral """
    sum = 0
    dx = interval / n

    for i in range(n):
        sum += func(x_1 + (i + 0.5) * dx) * dx

    return sum * (-1) ** reversed_check


# Main
print("Вычисление интеграла методом Срединных Прямоугольников.\n")
x_1, x_2 = None, None
reversed_check = 0

while x_1 is None and x_2 is None:
    x_1, x_2 = get_boundaries()
interval = x_2 - x_1

eps = float(input("Введите точность, с которой необходимо вычислить интеграл (Положительное число): "))
integral = true_integral_value()
print("Истинное значение интеграла: {:g}".format(integral))

# Algorithm
n = 1
while abs(middle_rectangle_method(func, interval, n) - middle_rectangle_method(func, interval, n * 2)) >= eps:
    n *= 2
print("Приближенное значение интеграла с заданной точностью {:} вычислено:\n"
      "Результат вычисления: {:g}".format(eps, middle_rectangle_method(func, interval, n)))









