"""
Беляев Никита, ИУ7-11б
Лабораторная работа №9. "Матрицы. Часть 2"

Задание:
Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
вводить. Транспонирование не применять.
"""

m = 0
check = 0
warning = ""

# We're asking for the input until it's correct
while m <= 0:
    if check > 0:
        warning = "Некорректный ввод. Повторите попытку. "
    m = int(input(warning + "Введите ранг матрицы: "))
    check += 1
print(f"Ваша матрица имеет ранг: {m}.\n")

# Fulfilling the matrix
matrix = []
for i in range(m):
    matrix.append(list(map(int, input(f"Введите символы {i + 1}-й строки через пробел: ").split(" "))))

# Showing  matrix
print("\nИсходная матрица:")
line = ""
for i in range(m):
    for j in range(m):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)

# Clockwise rotation: reverse elements in each line and mirror them by the 2nd diagonal
LAST_IDX = m - 1
for line in matrix:
    i = 0
    wall = m - 1    # Elements AFTER the wall in line are on their right positions
    for k in range(m - 1):
        while i < wall:
            line[i], line[i + 1] = line[i + 1], line[i]
            i += 1
        wall -= 1
        i = 0
for i in range(m):
    for j in range(LAST_IDX - (i + 1), -1, -1):
        # print(f">> I swap {matrix[i][j]} with {matrix[last_idx - j][last_idx - i]}")
        matrix[i][j], matrix[LAST_IDX - j][LAST_IDX - i] = matrix[LAST_IDX - j][LAST_IDX - i], matrix[i][j]

# Showing rotated matrix
print("\nМатрица после поворота по часовой стрелке на 90 градусов:")
line = ""
for i in range(m):
    for j in range(m):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)

# Rotating it back (Same algo with reversed steps)
for i in range(m):
    for j in range(LAST_IDX - (i + 1), -1, -1):
        # print(f">> I swap {matrix[i][j]} with {matrix[last_idx - j][last_idx - i]}")
        matrix[i][j], matrix[LAST_IDX - j][LAST_IDX - i] = matrix[LAST_IDX - j][LAST_IDX - i], matrix[i][j]
for line in matrix:
    i = 0
    wall = m - 1
    for k in range(m - 1):
        while i < wall:
            line[i], line[i + 1] = line[i + 1], line[i]
            i += 1
        wall -= 1
        i = 0

# Showing  matrix
print("\nМатрица после возвращения в исходное состояние:")
line = ""
for i in range(m):
    for j in range(m):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)





