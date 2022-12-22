"""
Защита 15-й
Удалить из бинарного файла все числа Фибоначчи.

Число Х является числом Фибоначчи тогда и только тогда, когда выражения 5 * X^2 +/- 4 - квадраты.
"""

import struct

format = "i"
TOKEN = struct.calcsize(format)

def add_numbers(file_path):
    size = int(input("Введите количество элементов в массиве: "))

    with open(file_path, "wb") as file:
        for i in range(size):
            number = int(input(f"Введите {i + 1}-й элемент: "))
            number_packed = struct.pack(format, number)
            file.write(number_packed)
    print("Вы ввели следующие числа: ")
    show_file(file_path, size)
    return size


def show_file(file_path, size):
    with open(file_path, "rb") as file:
        numbers = ""
        for i in range(size):
            number = file.read(TOKEN)
            number_unpacked = struct.unpack(format, number)[0]
            numbers += f" {number_unpacked} "
    print(numbers)


def deleter(file_path, size):
    with open(file_path, "rb+") as file:
        non_fibos_count = 0

        for i in range(size):
            file.seek(0, 0)
            file.seek(i * TOKEN, 0)
            number = file.read(TOKEN)
            number_unpacked = struct.unpack(format, number)[0]
            is_fibo = detect_fibo(number_unpacked)

            if not is_fibo:
                file.seek(non_fibos_count * TOKEN, 0)
                file.write(number)
                non_fibos_count += 1
        file.truncate(non_fibos_count * TOKEN)
    print("Из вашего файла удалены все числа Фибоначчи :(")
    show_file(file_path, non_fibos_count)


def detect_fibo(number):
    is_fibo = False
    if number < 0:
        return False

    test_equation_1 = (equation_1 := 5 * number ** 2 + 4) ** 0.5
    test_equation_2 = (equation_2 := 5 * number ** 2 - 4) ** 0.5

    # Print debugging
    print(f"Сканирую число {number}")

    if int(test_equation_1) == float(test_equation_1) or int(test_equation_2) == float(test_equation_2):
        is_fibo = True
    else:
        is_fibo = False

    # Print debugging
    print(f"Число {number} является числом Фибоначчи: {is_fibo}")

    return is_fibo


# Main
file_path = input("Введите путь к файлу: ")
size = add_numbers(file_path)
deleter(file_path, size)




