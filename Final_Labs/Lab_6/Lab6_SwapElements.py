'''
Беляев Никита
Вариант 2
Лабораторная работа №6 "Списки. Часть 1"

Программа 5. Обмен местами максимального и минимального элементов.
'''

print('Программа 5. Обмен местами максимального и минимального элементов.')

array = []
n = int(input("Введите количество элементов в массиве: "))
max_idx = 0
min_idx = 0

if n == 0:
    print('Введен пустой массив')
elif n == 1:
    array.append(int(input('Введите 1-й элемент массива: ')))
    print('Ваш массив:')
    print(array[0])
else:
    for i in range(n):
        array.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
        max_element = array[0]
        min_element = array[0]
        if array[i] > max_element:
            max_idx = i
            max_element = array[i]
        elif array[i] < min_element:
            min_idx = i
            min_element = array[i]
        else:
            continue
    print('Вы ввели массив:')
    print(*array)

    array[max_idx], array[min_idx] = array[min_idx], array[max_idx]
    print('Максимальный и минимальный элемент переставлены. Ваш массив:')
    print(*array)


