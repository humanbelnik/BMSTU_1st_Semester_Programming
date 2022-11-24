'''
Беляев Никита ИУ7-11б
Лабораторная работа №7.

Задание:
Найти элемент с наибольшим количеством английских гласных букв.
'''

print('Программа: Найти элемент с наибольшим количеством английских гласных букв. ')

# List input
words = []
n = int(input('Ввведите количество строк в массиве: '))
for i in range(n):
    words.append(str(input(f'Введите {i + 1}-ю строку массива: ')))
print('Вы ввели массив строк:')
print(*words)

# Algorithm
vowels = 'eyuioaAOIUYE'
max_amount = 0
target = None
for word in words:
    counter = 0
    for vowel in vowels:
        if vowel in word:
            counter += 1
    if counter > max_amount:
        target = word
if target is None:
    print('Введенные вами строки отсутствуют, либо не содержат гласных английсикх букв.')
else:
    print(f"Строка массива, содержащая больше всего английских гласных букв: {target}")




