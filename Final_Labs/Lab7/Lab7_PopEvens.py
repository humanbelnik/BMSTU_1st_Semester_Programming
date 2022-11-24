'''
Беляев Никита ИУ7-11б
Лабораторная работа №7.

Задание:
Удалить все четные элементы целочисленного списка за один цикл.
'''

print('Программа: Удалить все четные элементы целочисленного списка за один цикл.')
# List input
check = True
first = None
array = []
n = int(input('Ввведите количество элементов в массиве: '))
for i in range(n):
    array.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
    if check:
        if array[i] % 2 == 0:
            first = i
            check = False
print('Вы ввели массив:')
print(*array)

# Algo
if check:
    print('\nВ вашем массиве отсутствуют четные элементы. Ваш массив:')
    print(*array)
else:
    for i in range(first + 1, len(array), 1):
        if array[i] % 2 == 1:
            array[first], array[i] = array[i], array[first]
            first += 1
    array = array[:first]
    print('\nИз вашего массива удалены все четные элементы. Ваш массив:')
    print(*array)






