"""
Беляев Никита, ИУ7-11б
Лабораторная работа №9. "Матрицы. Часть 2"

Задача:
Сформировать матрицу C путём построчного перемножения матриц A и B
одинаковой размерности (элементы в i-й строке матрицы A умножаются на
соответствующие элементы в i-й строке матрицы B), потом сложить все
элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
A, B, C и массив V.
"""

# Inputs
m, n = 0, 0
check = 0
warning = ""

# We're asking for the input until it's correct
while m <= 0 or n <= 0:
    if check > 0:
        warning = "Некорректный ввод. Повторите попытку. "
    m, n = map(int, input(warning + "Введите размер матриц через пробел: ").split(" "))
    check += 1
print(f"Ваши матрицы будут содержать по {m} строк(-и) и {n} столбцов(-a).\n")

# Fulfilling matrices
print("Заполните матрицу А:")
a = []
b = []
for i in range(m):
    a.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

print("\nЗаполните матрицу B:")
b = []
for i in range(m):
    b.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

# Creating "C" matrix
c = []
for i in range(m):
    c.append([])
    for j in range(n):
        c[i].append(a[i][j] * b[i][j])

# Calculating column sums in "C" and saving them in "V"
v = []
for i in range(n):
    sum = 0
    for j in range(m):
        sum += c[j][i]
    v.append(sum)

# Showing the output

# A
print("\nМатрица А:")
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(a[i][j])
    line += "\n"
print(line)

# B
print("\nМатрица B:")
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(b[i][j])
    line += "\n"
print(line)

# C
print("\nМатрица С:")
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(c[i][j])
    line += "\n"
print(line)

# V
print(">> Суммы элементов в столбцах матрицы 'C' добавлены в массив 'V':\n ")
print("\nМассив V:")
line = ""
for element in v:
    line += "|{:^8g}|".format(element)
print(line)









