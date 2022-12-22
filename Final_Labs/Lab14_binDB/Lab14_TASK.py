"""
Защита ЛР 14:
"""
import struct

file_path = "./heights.bin"
FORMAT = "10si"
LINE_LENGTH = struct.calcsize(FORMAT)


def lines_counter(file_path):
    """ I return the amount of lines in database """
    with open(file_path, "rb") as file:
        file.seek(0, 2)
        full_size = file.tell()
        file.seek(0, 0)
        count_lines = full_size // LINE_LENGTH
    return count_lines


def add_line(file_path):
    surname = input("Введите фамилию участника: ")
    height = int(input("Введите рост участника (В см): "))
    print("Запись успешно добавлена!")

    packed = struct.pack(FORMAT, surname.encode("utf-8"), height)
    with open(file_path, "rb+") as file:
        file.seek(0, 2)
        file.write(packed)


def delete(file_path, j):
    with open(file_path, "rb") as file:
        file.seek(0, 2)
        full_size = file.tell()
    LINE_LENGTH = struct.calcsize("10s1i")
    wall = LINE_LENGTH * j

    with open(file_path, "rb+") as file:
        while wall < full_size:
            file.seek(wall + LINE_LENGTH)
            buffer = file.read(LINE_LENGTH)
            file.seek(wall)
            file.write(buffer)
            wall += LINE_LENGTH
        file.truncate(full_size - LINE_LENGTH)


def hook(file_path):
    hook = int(input("Введите значение роста, которое хотите удалить: "))
    count_lines = lines_counter(file_path)

    with open(file_path, "rb") as file:
        current_line = 1
        j = 0
        for line in range(count_lines):
            line = file.read(LINE_LENGTH)
            line = list(struct.unpack(FORMAT, line))
            if hook == line[1]:
                delete(file_path, j)
            j += 1




# Main:
while True:
    choice = int(input("Выберите действие:\n1 - Добавить запись\n2 - Удалить запись по значению роста\nВаш выбор: "))
    file_path = "./heights.bin"

    if choice == 1:
        add_line(file_path)
    elif choice == 2:
        hook(file_path)








