"""
Беляев Никита, ИУ7-11б
Лабораторная работа №9. "Матрицы. Часть 2"

Задача:
В матрице символов заменить все англисйкие гласные на точки.
"""

# Inputs
m, n = 0, 0
check = 0
warning = ""

# We're asking for the input until it's correct
while m <= 0 or n <= 0:
    if check > 0:
        warning = "Некорректный ввод. Повторите попытку. "
    m, n = map(int, input(warning + "Введите размер матрицы через пробел: ").split(" "))
    check += 1
print(f"Ваша матрица будет содержать {m} строк(-и) и {n} столбцов(-a).\n")

# Fulfilling the matrix
symbs = []
for i in range(m):
    symbs.append(list(input(f"Введите символы {i + 1}-й строки через пробел: ").split(" ")))

# Showing the raw matrix
print("Вы ввели следующую матрицу символов:")
for line in symbs:
    print(*line)

# Replacing english vowels with dots
vowels = ["e", "E", "y", "Y", "u", "U", "i", "I", "e", "E", "a", "A", "o", "O"]
for line in symbs:
    for idx, symb in enumerate(line):
        if symb in vowels:
            line[idx] = "."

# Showing the edited matrix
print("Все гласные английские символы вашей матрицы заменены на точки: ")
for line in symbs:
    print(*line)







