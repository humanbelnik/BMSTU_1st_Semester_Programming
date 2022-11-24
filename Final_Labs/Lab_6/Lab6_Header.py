'''
ИУ7-11б
Беляев Никита
Вариант 2
Лабораторная работа №6 "Списки. Часть 1"

Описание:
Работа включается в себя 8 файлов. Файлы, исполняющие команды 1 - 7 подключены к основному в виде модулей
'''

MENU_WIDTH = 75

# Menu printing
print(
    '|' + '-' * MENU_WIDTH + '|' + "\n" +
    '|' + "\033[1m" + f"{'Работа с целочисленным массивом':^{MENU_WIDTH}}" + "\033[0m" + '|' + '\n'
    '|' + '-' * MENU_WIDTH + '|' + '\n'                                                                                            
    '|' + f"{'      1. Добавить элемент по индексу с использованием ср-в Python-a':<{MENU_WIDTH}}" + '|' + "\n" +
    '|' + f"{'      2. Добавить элемент по индексу алгоритмически':<{MENU_WIDTH}}" + '|' + "\n" +
    '|' + f"{'      3. Удалить элемент по индексу с использованием ср-в Python-a':<{MENU_WIDTH}}" + '|' + "\n" +
    '|' + f"{'      4. Удалить элемент по индексу алгоритмически':<{MENU_WIDTH}}" + '|' + "\n" +
    '|' + f"{'      5. Найти К-й экстремум в списке':<{MENU_WIDTH}}" + '|' + "\n" +
    '|' + f"{'      6. Найти наибольшую последовательность возрастающих целых чисел':<{MENU_WIDTH}}" + '|' + "\n" +
    '|' + f"{'      7. Переставить местами максимальный и минимальный элемент':<{MENU_WIDTH}}" + '|' + "\n" +
    '|' + '-' * MENU_WIDTH + '|'
)
choice = int(input("Выберите команду из списка по номеру: "))

if choice == 1:
    import Lab6_AddFast
elif choice == 2:
    import Lab6_AddAlgo
elif choice == 3:
    import Lab6_DelFast
elif choice == 4:
    import Lab6_DelAlgo
elif choice == 5:
    import Lab6_FindExtremum
elif choice == 6:
    import Lab6_FindSequence
elif choice == 7:
    import Lab6_SwapElements
else:
    print('Ошибка. Команда не найдена')

