"""
Беляев Никита ИУ711-б
Лабораторная работа №15 "Бинарный файл". (1/3)

Задание:
Из бинарного файла с целочисленым 32-х битным наполнением удалить четные числа за один проход по файлу
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
    if nums == "":
        print("Вы удалили все числа!")
    else:
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


def delete_evens(file_path, size):
    """
    1. We iterate through the whole list element-by-element, checking if it's odd.
    2. If it's even -> check the next
    3. If it's odd -> write in at the beginning of the "NOT EVEN" sequence at the beginning of the file
    """
    with open(file_path, "rb+") as file:
        odds_count = 0
        for i in range(size):
            file.seek(0, 0)
            file.seek(i * NUM_LENGTH, 0)
            number = file.read(NUM_LENGTH)
            number_unpacked = struct.unpack(format, number)[0]
            if number_unpacked % 2 != 0:
                # print(f"I save {number_unpacked}")
                file.seek(odds_count * NUM_LENGTH, 0)
                file.write(number)
                odds_count += 1
        evens_count = size - odds_count
        file.truncate(odds_count * NUM_LENGTH)
    if evens_count == 0:
        message = "В вашем файле отсутствуют четные числа."
    else:
        message = "Из вашего файла удалены все четные числа."
    show_file(file_path, odds_count, message)


if __name__ == "__main__":
    file_path = get_file()
    size = fulfill_file(file_path)
    delete_evens(file_path, size)


