# Input & fulfill
matrix = []
m, n = map(int, input("Введите размер матрицы (Кол-во строк и столбцов) через пробел: ").split(" "))
for i in range(m):
    matrix.append(list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split(" "))))

# Algo
i = 0
while i < m:
    print(f">> Now i scan line {i}")
    for j in range(n):  # Scan "i" line
        if matrix[i][j] == 0:
            matrix.insert(i + 1, [x * 2 for x in matrix[i]])
            i += 1
            m += 1
            break  # One "0" in line is enough. Go to the next line.
    i += 1

# Output
line = ""
for i in range(m):
    for j in range(n):
        line += "|{:^8g}|".format(matrix[i][j])
    line += "\n"
print(line)



