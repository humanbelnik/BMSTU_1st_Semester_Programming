'''
ИУ7-11б
Беляев Никита
Вариант 2
Лабораторная работа №6 "Списки. Часть 1"

Программа 1b. Удаление элемента по индексу c использованием средств Python-a.
'''

print('Программа 2b. Удаление элемента по индексу алгоритмически.')

# Init and fulfill the array
array = []
n = int(input("Введите количество элементов в массиве: "))
for i in range(n):
    array.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
print('Вы ввели массив:')
print(*array)

if len(array) == 0:
    print("Массив не содержит элементов. Удалять нечего. Повторите ввод.")
else:
    # Command
    del_idx = int(input('Введите индекс элемента, который хотите удалить: '))
    if del_idx > len(array):
        print("Индекс выходит за размер массива. Будет удален последний элемент.")
    for i in range(del_idx, len(array) - 1):
        array[i] = array[i + 1]
    del array[len(array) - 1]
    print(f'Элемент успешно удален. Ваш массив:')
    print(*array)
