"""
Беляев Никита ИУ7-11б
Л.Р №8 "Матрицы. Часть 1"

Задание:
Переставить местами столбцы с максимальной и минимальной суммой
элементов.
"""

# Input
print("\nПрограмма: Переставить местами столбцы с максимальной и минимальной суммой элементов.\n")

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

# Algo
sum_max, sum_min = float("-inf"), float("+inf")
idx_max, idx_min = 0, 0

for i in range(n):
    summa = 0
    for j in range(m):
        summa += matrix[j][i]
    if summa > sum_max:
        sum_max = summa
        idx_max = i
    if summa < sum_min:
        sum_min = summa
        idx_min = i
for k in range(m):
    matrix[k][idx_max], matrix[k][idx_min] = matrix[k][idx_min], matrix[k][idx_max]

# Final output
print("Столбцы с максимальной и минимальной суммой элементов переставлены местами:")
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)



