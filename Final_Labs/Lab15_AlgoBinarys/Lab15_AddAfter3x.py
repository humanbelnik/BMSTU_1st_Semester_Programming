"""
Беляев Никита ИУ711-б
Лабораторная работа №15 "Бинарный файл". (2/3)

Задание:
В бинарном файле с целочисленным 32-х битным наполнением вставить после каждого кратного 3-м элемента его
удвоенное значение за <= 2 прохода по файлу.
"""


import struct
import CheckValues as check
import os

NUM_LENGTH = struct.calcsize("i")
format = "i"


def get_file():
    """ I'm asking User for file path input """
    file_path = None
    while file_path is None:
        print("\n>> Текущая директория:")
        os.system("pwd")
        print("\n>> Название файла не должно содержать пробелов.")
        file_path = check.get_solid_input("Укажите путь к файлу, который хотите заполнить числами: ")

        if ".py" in file_path:
            print("(!) Файл может содержать программный код. Пожалуйста, повторите ввод.")
            file_path = None
            continue

        try:
            file = open(file_path, "wb")
            file.close()
        except:
            print("Файл указан некорректно. Пожалуйста, повторите ввод.")
            file_path = None

        print(f"\n>> Для работы установлен файл: {file_path}")
    return file_path


def show_file(file_path, size, message):
    """ I show file's content """
    with open(file_path, "rb") as file:
        nums = ""
        for i in range(size):
            number = file.read(NUM_LENGTH)
            number_unpacked = struct.unpack(format, number)[0]
            nums += f" {number_unpacked} "
    print(message)
    print(nums)


def fulfill_file(file_path):
    """ I add numbers to a file """
    size = check.get_positive_integer("Введите количество элементов в списке: ")
    with open(file_path, "wb") as file:
        for i in range(size):
            number = check.get_integer(f"Введите {i + 1}-е число: ")
            number_packed = struct.pack(format, number)
            file.write(number_packed)
    message = "Вы ввели следующую последовательность чисел: "
    show_file(file_path, size, message)
    return size


def get_size_and_count(file_path):
    with open(file_path, "rb") as file:
        file.seek(0, 2)
        full_size = file.tell()
        numbers_count = full_size // NUM_LENGTH
        file.seek(0, 0)
    return full_size, numbers_count


def add_numbers(file_path):
    with open(file_path, 'rb+') as file:
        full_size, numbers_count = get_size_and_count(file_path)

        j = 0
        while j < numbers_count:
            file.seek(j * NUM_LENGTH)
            number = file.read(NUM_LENGTH)
            number_unpacked = struct.unpack(format, number)[0]

            if number_unpacked % 3 == 0:
                new_number = number_unpacked * 2
                if new_number > 2_147_483_647 or new_number < -2_147_483_648:
                    new_number = 0
                new_number_packed = struct.pack(format, new_number)

                for i in range(numbers_count, j, -1):
                    file.seek(i * NUM_LENGTH, 0)
                    buffer = file.read(NUM_LENGTH)
                    file.write(buffer)
                file.seek(NUM_LENGTH * (j + 1))
                file.write(new_number_packed)
                j += 1
                numbers_count += 1
            j += 1

    full_size, numbers_count = get_size_and_count(file_path)
    show_file(file_path, numbers_count, "(!) Если в вашем списке было число кратное 3-м, удвоенное значение которого "
                                        "не входит в диапазон 4-х байт, то после него был вставлен 0.\nВаша "
                                        "последовательность чисел отредактирована:")


if __name__ == "__main__":
    file_path = get_file()
    size = fulfill_file(file_path)
    add_numbers(file_path)
