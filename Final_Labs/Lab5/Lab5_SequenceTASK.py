'''
Беляев Никита
ИУ7-11б
Защита лабораторной работы №4
'''

# Блок ввода
x = float(input("Введите значение аргумента: "))
eps = float(input("Введите значение необходимой точности вычисления суммы (Положительное число): "))

# Необходимые параметры
n = 1  # Счетчик
sum = 1  # Сумма
current_top = x ** 2  # Числитель
current_low = 2  # Знаменатель
current = current_top/current_low  # Первое слагаемое ряда
print(current)


while abs(current) >= eps:  # Считаем сумму до тех пор, пока слагаемые не меньше точности.
    sum += current
    current_top = (current_top + 2 * x ** (2 * n)) * (x ** 2)
    current_low = current_low * (2 * n + 1) * (2 * n + 2)
    current = (-1) ** n * (current_top / current_low)
    n += 1
    print(current)
sum += current
print('Конечная сумма ряда: {:g}'.format(sum))




