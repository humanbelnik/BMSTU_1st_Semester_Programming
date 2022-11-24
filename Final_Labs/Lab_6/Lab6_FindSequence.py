'''
Беляев Никита
Вариант 2
Лабораторная работа №6 "Списки. Часть 1"

Программа 4. Нахождение наибольшей по длине непрерывной возрастающей последовательности целых чисел.
'''

print('Программа 4. Нахождение наибольшей по длине непрерывной возрастающей последовательности целых чисел.')

# Current sequence
first_current_idx = 0
last_current_idx = 0
length = last_current_idx - first_current_idx

# Max-length sequence
first_max_idx = 0
last_max_idx = 0
length_max = last_max_idx - first_max_idx

single = True

# Init and fulfill the array
array = []
n = int(input("Введите количество элементов в массиве: "))
for i in range(n):
    array.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
print('Вы ввели массив:')
print(*array)

if len(array) == 0:
    print("Массив пуст. Повторите ввод")
else:
    i = 0
    while i < len(array) - 1:
        j = i
        first_current_idx = j
        while array[j + 1] > array[j]:
            last_current_idx += 1
            j += 1
            if j + 1 > len(array) - 1:
                break
        length = last_current_idx - first_current_idx + 1

        # Comparing current and maximum lengths
        if length > length_max:
            last_max_idx = last_current_idx  # 1
            first_max_idx = first_current_idx  # 0
            length_max = length  # 2
        elif length == length_max:
            single = False
        i += length
        last_current_idx += 1

    if len(array) == 1:
        print(f'В вашем массиве один элемент. Он и есть наибольшая последовательность: {array[0]}')
    else:
        if single:
            print('Наибольшая непрерывная возрастаяющая последовательность целых чисел: ')
        else:
            print(
                'В вашем массиве несколько последовательностей одинаковой длины, большей, чем остальные. Первая из них: \n')
        for i in range(first_max_idx, last_max_idx + 1):
            print(array[i])







