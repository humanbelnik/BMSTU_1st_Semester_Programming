"""
Беляев Никита, ИУ7-11б
Лабораторная работа №9. "Матрицы. Часть 2"

Задача:
Подсчитать в каждой строке матрицы D количество элементов, превышающих
суммы элементов соответствующих строк матрицы Z. Разместить эти
количества в массиве G, умножить матрицу D на максимальный элемент
массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
также массив G
"""

# Inputs
m_z, n_z = 0, 0
m_d, n_d = 0, 0
check = 0
warning = ""

# We're asking for the input for matrix "Z" until it's correct
while m_z <= 0 or n_z <= 0:
    if check > 0:
        warning = "Некорректный ввод. Повторите попытку. "
    m_z, n_z = map(int, input(warning + "Введите размер матрицы Z через пробел: ").split(" "))
    check += 1
print(f"\n>> Матрица Z содержит {m_z} строк(-и) и {n_z} столбцов(-a).\n")
check = 0
warning = ""

# Fulfilling the matrix "Z"
z = []
for i in range(m_z):
    z.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

# We're asking for the input for matrix "D" until it's correct
while m_d <= 0 or n_d <= 0:
    if check > 0:
        warning = "Некорректный ввод. Повторите попытку. "
    m_d, n_d = map(int, input(warning + "Введите размер матрицы D через пробел: ").split(" "))
    check += 1
print(f"\n>> Матрица D содержит {m_d} строк(-и) и {n_d} столбцов(-a).\n")
check = 0
warning = ""

# Fulfilling the matrix "D"
d = []
for i in range(m_d):
    d.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

scan_area = m_d    # Number of lines we're gonna compare (In order to not catch "Index out of range" error)
if m_z < m_d:
    scan_area = m_z

# Algo
g = []
for i in range(scan_area):   # Iter through "D" lines
    sum = 0  # sum of elements in current "Z" line
    counter = 0
    for j in range(n_z):   # Iter through "Z" line
        sum += z[i][j]
    # now we have a sum
    for k in range(n_d):
        if d[i][k] > sum:
            counter += 1
    # now we have what we need
    g.append(counter)

# Finding max in "G"
max_elem = g[0]
for element in g:
    if element > max_elem:
        max_elem = element

# Output

# Z
print("\nМатрица Z:")
line = ""
for i in range(m_z):
    for j in range(n_z):
        line += "|{:^8g}|".format(z[i][j])
    line += "\n"
print(line)

# D previous
print("\nИсходная матрица D:")
line = ""
for i in range(m_d):
    for j in range(n_d):
        line += "|{:^8g}|".format(d[i][j])
    line += "\n"
print(line)

# D after editing
print("\nМатрица D после редактирования (Домножена на максимальный элемент массива G):")
line = ""
for i in range(m_d):
    for j in range(n_d):
        line += "|{:^8g}|".format(d[i][j] * max_elem)
    line += "\n"
print(line)

# G
print("\nМассив G:")
line = ""
for element in g:
    line += "|{:^8g}|".format(element)
print(line)




