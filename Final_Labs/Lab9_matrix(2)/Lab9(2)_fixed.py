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

# Algo
temp = None
rings = m // 2
last_idx = m - 1

# Clockwise
for i in range(rings):
    for j in range(i, last_idx - i):
        #print(f">>> {matrix[i][j]}\n {matrix[last_idx - j][i]}\n {matrix[last_idx - i][last_idx - j]}\n {matrix[j][last_idx - i]}")
        temp = matrix[i][j]
        matrix[i][j] = matrix[last_idx - j][i]  # UP LEFT = DOWN LEFT
        matrix[last_idx - j][i] = matrix[last_idx - i][last_idx - j]  # DOWN LEFT = DOWN RIGHT
        matrix[last_idx - i][last_idx - j] = matrix[j][last_idx - i]  # DOWN RIGHT = UP RIGHT
        matrix[j][last_idx - i] = temp  # UP RIGHT = UP LEFT

print("Матрица после поворота по часовой стрелке: ")
line = ""
for i in range(m):
    for j in range(m):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)

# Getting it back
for i in range(rings):
    for j in range(i, last_idx - i):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][last_idx - i]   # UP LEFT = UP RIGHT
        matrix[j][last_idx - i] = matrix[last_idx - i][last_idx - j]    # UP RIGHT = DOWN RIGHT
        matrix[last_idx - i][last_idx - j] = matrix[last_idx - j][i]    # DOWN RIGHT = DOWN LEFT
        matrix[last_idx - j][i] = temp

print("Матрица возвращена в исходное состояние: ")
line = ""
for i in range(m):
    for j in range(m):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)













