"""
Беляев Никита ИУ7-11б
Л.Р №8 "Матрицы. Часть 1"

Задание:
Найти строку, имеющую наибольшее количество одинаковых и под ряд идущих элементов
"""

# Input
print("\nПрограмма: Найти строку, имеющую наибольшее количество одинаковых под ряд идущих элементов.\n")

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

# Finding the line
rows = []
greater_line = 0
index = 0
for k in range(len(matrix)):      # I'm iterating through lines
    i = 0
    streak = 1
    row_max = 1
    while i < len(matrix[k]) - 1:      # I return "row_max" - the longest sequence in line
        j = i
        while matrix[k][j + 1] == matrix[k][j]:
            streak += 1
            j += 1
            if j + 1 > len(matrix[k]) - 1:
                break
        if streak > row_max:
            row_max = streak
        i += streak
        streak = 1
    if row_max > greater_line:
        greater_line = row_max
        index = k

# Output
print(f"Строка #{index + 1} имеет наибольшее количество под ряд идущих одинаковых элементов:")
line = ""
for i in range(n):
    line += "|{:^8g}|".format(matrix[index][i])
line += "\n"
print(line)
















