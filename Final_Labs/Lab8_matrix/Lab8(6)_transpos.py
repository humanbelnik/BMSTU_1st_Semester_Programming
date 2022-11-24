"""
Беляев Никита ИУ7-11б
Л.Р №8 "Матрицы. Часть 1"

Задание:
Транспонирование квадратной матрицы

Логика:
1) Проходимся только по врехнему треугольнику матрицы, обменивая симметричные элементы
"""

# Input
print("\nПрограмма: Транспонирование квадратной матрицы.\n")

matrix = []
m = 0
check = 0
while m == 0:
    if check > 0:
        warning = "Вы ввели пустую матрицу. Повторите ввод.\n"
    else:
        warning = ""
    m = int(input(warning + "Введите ранг матрицы: "))
    check += 1
for i in range(m):
    matrix.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

# Output
print("\nВы ввели матрицу:")
line = ""
for i in range(m):
    for j in range(m):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)

# Transposition
for i in range(m):
    for j in range(i + 1, m):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Output the final result
print("Матрица транспонирована:")
line = ""
for i in range(m):
    for j in range(m):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)


