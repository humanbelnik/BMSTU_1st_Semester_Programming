"""
Беляев Никита, ИУ7-11б
Лабораторная работа №9. "Матрицы. Часть 2"

Задача:
Даны массивы D и F. Сформировать матрицу A по формуле
a(jk) = sin( d(j) + f(k) ).
Определить среднее арифметическое положительных чисел каждой строки
матрицы и количество элементов, меньших среднего арифметического.
Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
виде матрицы и рядом столбцы AV и L.

D - lines
F - columns
"""

from math import sin

# Inputs
d = []
f = []
D_size, F_size = 0, 0
check = 0
warning = ""

# Fulfill "D"
while D_size <= 0:
    if check > 0:
        warning = "Некорректный ввод. Длина массива неотрицательна. Повторите."
    D_size = int(input(warning + "Введите длину массива D: "))
    check += 1
warning = ""
check = 0
d = list(map(float, input("Введите элементы массива D через пробел: ").split(" ")))

# Fulfill "F"
while F_size <= 0:
    if check > 0:
        warning = "Некорректный ввод. Длина массива неотрицательна. Повторите."
    F_size = int(input(warning + "Введите длину массива F: "))
    check += 1
warning = ""
check = 0
f = list(map(float, input("Введите элементы массива D через пробел: ").split(" ")))

# Making "A"
a = [[0 for x in range(F_size)] for x in range(D_size)]
for i in range(D_size):
    for j in range(F_size):
        a[i][j] = sin(d[i] + f[j])

# Calculating AL and L
av = []
l = []
for line in a:
    avg, sum = 0, 0
    counter = 0  # Count amount of nums which are less then average
    pos_counter = 0  # Count amount of positive nums in line
    for element in line:
        if element > 0:
            sum += element
            pos_counter += 1
    if pos_counter != 0:
        avg = sum/pos_counter
    for element in line:
        if element < avg:
            counter += 1
    av.append(avg)
    l.append(counter)

# Output
print("\nМатрица A и значения из AV и L в последних двух колонках:")
line = ""
for i in range(D_size):
    for j in range(F_size):
        line += "|{:^12g}|".format(a[i][j])
    line += "     |{:^8.5g}| {:^8.5g}|".format(av[i], l[i])
    line += "\n"
print(line)



