'''
ИУ7-11б
Беляев Никита
Вариант 2
Лабораторная работа №6 "Списки. Часть 1"

Программа 1b. Добавление элемента по индексу алгоритмически.
'''

print('Программа 1b. Добавление элемента по индексу алгоритмически.')

# Init and fulfill the array
array = []
n = int(input("Введите количество элементов в массиве: "))
for i in range(n):
    array.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
print('Вы ввели массив:')
print(*array)

# Command
new = int(input('Введите новый элемент: '))
new_idx = int(input('Введите индекс позиции, на которую вы хотите вставить элемент: '))

if new_idx > len(array):
    array.append(new)
    print("Индекс новго элемента выходит за размеры массива. Элемент добавлен на последнюю позицию.\nВаш массив:")
    print(*array)
else:
    array.append(0)
    for i in range(len(array) - 2, new_idx - 1, -1):
        array[i + 1] = array[i]
    array[new_idx] = new
    print('Элемент успешно добавлен. Ваш массив:')
    print(*array)


