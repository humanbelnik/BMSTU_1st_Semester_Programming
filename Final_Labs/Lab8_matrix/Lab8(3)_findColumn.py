"""
Беляев Никита ИУ7-11б
Л.Р №8 "Матрицы. Часть 1"

Задание:
Найти столбец, содержащий наибольшее количество простых чисел
"""

import math as m

# Input
print("\nПрограмма: Найти столбец, содержащий наибольшее количество простых чисел.\n")

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
max_primes = 0
column = 0
for i in range(n):  # Иду по столбцам
    counter = 0
    for j in range(m):
        element = matrix[j][i]
        if element <= 0 or element == 1 or int(element) != element:
            continue
        is_prime = True
        div = element - 1
        while div > 1:
            if element % div == 0:
                is_prime = False
                break
            div -= 1
        if is_prime:
            counter += 1
            # print(f"elem {element} is prime ")
    # print(f"col {i + 1} has {counter} primes")
    if counter > max_primes:
        max_primes = counter
        column = i


# Final output
print(f"Столбец #{column + 1} имеет наибольшее количество простых чисел:")
line = ""
for i in range(m):
    line += "|{:^8g}|\n".format(matrix[i][column])
line += "\n"
print(line)





