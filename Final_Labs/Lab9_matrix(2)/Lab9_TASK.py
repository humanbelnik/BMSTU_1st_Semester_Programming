"""
матрица символов
удалить все строки, в которых цифр больше букв
"""

symbs = []
m, n = map(int,input("Введите размер матрицы через пробел (M x N): ").split(" "))
print(f"Количество строк: {m}\nКоличество столбцов: {n}\n")

for i in range(m):
    symbs.append(list(input(f"Введите символы {i + 1}-й строки через пробел: ").split(" ")))

print("Вы ввели следующую матрицу символов:")
for line in symbs:
    print(*line)

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

OVERALL = n
line = 0
while line < m:
    nums_counter = 0
    for element in symbs[line]:
        if element in nums:
            nums_counter += 1
    if nums_counter > OVERALL - nums_counter:
        symbs.pop(line)
        m -= 1
        line -= 1
    line += 1

print("Из матрицы удалены строки, в которых цифр больше, чем букв:")
if len(symbs) == 0:
    print("В матрице отсутствуют элементы")
else:
    for line in symbs:
        print(*line)

