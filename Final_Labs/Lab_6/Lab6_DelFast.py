'''
ИУ7-11б
Беляев Никита
Вариант 2
Лабораторная работа №6 "Списки. Часть 1"

Программа 1b. Удаление элемента по индексу c использованием средств Python-a.
'''

print('Программа 1b. Удаление элемента по индексу c использованием средств Python-a.')

# Init and fulfill the array
array = []
n = int(input("Введите количество элементов в массиве: "))
for i in range(n):
    array.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
print('Вы ввели массив:')
print(*array)
# Command
del_idx = int(input('Введите индекс элемента, который хотите удалить: '))
array.pop(del_idx)

print(f'Элемент успешно удален. Ваш массив: {array}')