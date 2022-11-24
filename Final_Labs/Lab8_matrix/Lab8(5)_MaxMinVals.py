"""
Беляев Никита ИУ7-11б
Л.Р №8 "Матрицы. Часть 1"

Задание:
В квадратной матрице найти максимальное значение над главной диагональю и минимальное под побочной.
"""

# Input
print("\nПрограмма: В квадратной матрице найти максимальное значение над главной диагональю и минимальное под побочной.\n")

matrix = []
m = 0
check = 0
while m <= 1:
    if check > 0:
        warning = "Ввод некорректен. Ранг должен быть больше 1. Повторите ввод.\n"
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

# Finding max value UPPER:
element_max = matrix[0][1]
for i in range(m):
    for j in range(i + 1, m):
        element = matrix[i][j]
        if element > element_max:
            element_max = element

# Finding min value UNDER:
element_min = matrix[1][m - 1]
for i in range(m - 1, 0, -1):
    for j in range(m - i, m, 1):
        element = matrix[i][j]
        if element < element_min:
            element_min = element

# Output
print("Максимальное значение над главной диагональю: {:g}\nМинимальное значение под побочной диагональю: {:g}".format(element_max, element_min))

