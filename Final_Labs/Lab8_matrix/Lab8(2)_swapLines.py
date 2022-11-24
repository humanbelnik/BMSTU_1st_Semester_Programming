"""
Беляев Никита ИУ7-11б
Л.Р №8 "Матрицы. Часть 1"

Задание:
Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов
"""

# Input
print("\nПрограмма: Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов.\n")

matrix = []
m, n = 0, 0
check = 0
while m == 0 or n == 0:
    if check > 0:
        warning = "Вы ввели пустую матрицу. Повторите ввод.\n"
    else:
        warning = ""
    m, n = map(int, input(warning + "Введите количество строк и столбцов матрицы через пробел: ").split(" "))
    check += 1
for i in range(m):
    matrix.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

# Output
print("\nВы ввели матрицу:")
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)

# Swapping
less_neg = n + 1
most_neg = 0
less_idx = 0
most_idx = 0
for i in range(m):
    counter = 0
    for j in range(n):
        if matrix[i][j] < 0:
            counter += 1
    if counter > most_neg:
        most_neg = counter
        most_idx = i
    if counter < less_neg:
        less_neg = counter
        less_idx = i
matrix[most_idx], matrix[less_idx] = matrix[less_idx], matrix[most_idx]

# Output the final result
print("Строки с наибольшим и наименьшим кол-вом отрицательных элементов переставлены местами:")
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)
