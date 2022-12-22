"""
Беляев Никита ИУ711-б
Лабораторная работа №15 "Бинарный файл". (3/3)

Задание:
Отсортировать числа, входящие в 32-х битный диапазон, методом Шейкер сортировки в бинарном файле.
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


def show_file(file_path, size,  message):
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


def shaker_sort_binary(file_path):
    with open(file_path, "rb+") as file:
        left_wall = 0
        full_size, numbers_count = get_size_and_count(file_path)
        right_wall = numbers_count - 1
        sorted = False

        while not sorted:
            sorted = True

            # If there will be no swaps, array is already sorted -> we'll break
            for i in range(left_wall, right_wall):
                file.seek(i * NUM_LENGTH, 0)

                current_number = file.read(NUM_LENGTH)
                current_number_unpacked = struct.unpack(format, current_number)[0]
                next_number = file.read(NUM_LENGTH)
                next_number_unpacked = struct.unpack(format, next_number)[0]

                if current_number_unpacked > next_number_unpacked:
                    file.seek(-2 * NUM_LENGTH, 1)
                    file.write(next_number)
                    file.write(current_number)
                    sorted = False

            if sorted:
                break

            sorted = True
            right_wall -= 1

            for i in range(right_wall, left_wall - 1, -1):
                file.seek(i * (NUM_LENGTH - 2))

                next_number = file.read(NUM_LENGTH)
                next_number_unpacked = struct.unpack(format, next_number)[0]
                current_number = file.read(NUM_LENGTH)
                current_number_unpacked = struct.unpack(format, current_number)[0]

                if current_number_unpacked < next_number_unpacked:
                    file.seek(-2 * NUM_LENGTH, 1)
                    file.write(current_number)
                    file.write(next_number)
                    sorted = False

            left_wall += 1
    show_file(file_path, numbers_count, "Числа успешно отсортированы:")


if __name__ == "__main__":
    file_path = get_file()
    size = fulfill_file(file_path)
    shaker_sort_binary(file_path)