"""
Беляев Никита, ИУ7-11б
Лабораторная работа №9. "Матрицы. Часть 2"

Задача:
Задана матрица D и массив I, содержащий номера строк, для которых
необходимо определить максимальный элемент. Значения максимальных
элементов запомнить в массиве R. Определить среднее арифметическое
вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
среднее арифметическое значение.
"""

# Inputs
m, n = 0, 0
check = 0
warning = ""

# We're asking for the input until it's correct
while m <= 0 or n <= 0:
    if check > 0:
        warning = "Некорректный ввод. Повторите попытку. "
    m, n = map(int, input(warning + "Введите размер матрицы через пробел: ").split(" "))
    check += 1
print(f"Ваша матрица будет содержать по {m} строк(-и) и {n} столбцов(-a).\n")
check = 0
warning = ""

# Fulfilling the matrix
d = []
for i in range(m):
    d.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

# Asking for the amount of lines User wants to process
# Aslo check if the amount of lines is bigger than amount of lines in matrix
lines = []
lines_size = m + 1
while lines_size > m:
    if check > 0:
        warning = f"Некорректный ввод. Количество строк в матрице: {m}. "
    lines_size = int(input(warning + "Введите количество строк, которые вы хотите обработать: "))
    check += 1

# Asking for the exact numbers of lines User wants to process
for i in range(lines_size):
    index = m
    check = 0
    warning = ""
    while index > m - 1 or index < 0:
        if check > 0:
            warning = "Строки с таким номером в матрице нет. Повторите ввод. "
        index = int(input(warning + "Введите номер строки, которую хотите обработать: ")) - 1
        check += 1
    lines.append(index + 1)

# Iterating through picked lines and finding the MAX element
r = []
elem = None
elem_idx = 0
for i in range(len(lines)):
    elem = d[lines[i] - 1][0]
    for j in range(n):
        if d[lines[i] - 1][j] > elem:
            elem = d[lines[i] - 1][j]
            elem_idx = j
    r.append(elem)

# Finding the average of maxes
avg, sum = 0, 0
for element in r:
    sum += element
if len(r) > 0:
    avg = sum/len(r)

# Output

# D
print("\nМатрица D:")
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(d[i][j])
    line += "\n"
print(line)

# I
print("\nМассив I:")
line = ""
for element in lines:
    line += "|{:^8g}|".format(element)
print(line)

# R
print("\nМассив R:")
line = ""
for element in r:
    line += "|{:^8g}|".format(element)
print(line)

# Average
print("Среднее арифметическое максимальных элементов в выбранных строках: {:g}".format(avg))












