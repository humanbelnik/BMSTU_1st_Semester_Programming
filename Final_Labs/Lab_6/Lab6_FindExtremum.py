'''
ИУ7-11б
Беляев Никита
Вариант 2
Лабораторная работа №6 "Списки. Часть 1"

Программа 3. Нахождение K-го экстремума.
'''

print('Программа 3. Нахождение K-го экстремума.')

# Init and fulfill the array
array = []
n = int(input("Введите количество элементов в массиве: "))
for i in range(n):
    array.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
print('Вы ввели массив:')
print(*array)
# Command
# I go from the 2nd to the (Last - 1) element and compare it with it's neighbours.
key = int(input('Введите номер экстремума: '))
counter = 0
for i in range(1, len(array) - 1):
    current = array[i]
    last = array[i - 1]
    next = array[i + 1]
    extremum = None
    if (current > last and current > next) or (current < last and current < next):
        counter += 1
        extremum = current
    if counter == key:
        print(f'{key}-й экстремум списка: {extremum}')
        break
else:
    print('Экстремум не найден')