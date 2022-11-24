"""
Беляев Никита, ИУ7-11б
Лабораторная работа №9. "Матрицы. Часть 2"

Задание:
Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
индексов начинается с 1)
"""

print("\n >> Ориентация осей: X - вправо, Y - вверх, Z - вглубь экрана\n")
# Inputs
x, y, z = 0, 0, 0
check = 0
warning = ""

# We're asking for the input until it's correct
while x <= 0 or y <= 0 or z <= 0:
    if check > 0:
        warning = "Некорректный ввод. Повторите попытку. "
    x, y, z = map(int, input(warning + "Введите размер (X * Y * Z) трехмерной матрицы через пробел: ").split(" "))
    check += 1
print(f"Ваша трехмерная матрица имеет размеры:\nКоличество столбцов (Ширина): "
      + f"{x}\nКоличество строк (Высота): {y}\nКоличество слоев (Глубина): {z}\n")
check = 0
warning = ""

# Fulfilling matrix
matrix = []
print("Заполните матрицу:")
for i in range(z):
    matrix.append([])
    for j in range(y):
        matrix[i].append(list(map(float, input(f"Введите {x} элементов {j + 1}-й строки {i + 1}-го слоя: ").split(" "))))

# Showing matrix
print("Вы ввели матрицу (Вывод послойно от ближнего к дальнему):")
line = ""
for i in range(z):
    for j in range(y):
        for k in range(x):
            line += "|{:^8g}|".format(matrix[i][j][k])
        line += "\n"
    line += "\n"
print(line)

#
layer = y
while layer > y - 1 or layer < 0:
    if check > 0:
        warning = "Ошибка. Данного среза не существует. Повторите ввод. "
    layer = int(input(warning + "Введите номер среза (Горизонтального слоя), который хотите вывести: ")) - 1
    check += 1

# Showing slice
print("")
line = ""
for i in range(z):
    for j in range(x):
        line += "|{:^8g}|".format(matrix[i][y - layer - 1][j])
    line += "\n"
print(line)



