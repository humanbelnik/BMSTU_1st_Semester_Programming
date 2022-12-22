"""
Беляев Никита, ИУ711-б.
Лабораторная работа №14. "База данных в бинарном файле".

Задание:
С помощью консольного меню организовать базу данных в бинарном файле.
Тестовый файл: ./todobin
"""

import os
import CheckValues as check
import struct

LINE_LENGTH = struct.calcsize("38s23s10s1b")

def check_file(file_path, message):
    """ I check if the file path is correct """
    try:
        file = open(file_path, "ab")
        file.close()
    except:
        print(message)
        return None
    return file_path


def check_database(file_path, message):
    """
    I check if there's a DB or an ability to make it a DB without clearing it out.
        - return 0 means that file is empty
        - return 1 means that file already has a DB
        - return None means that file is filled with something
    """

    with open(file_path, "rb") as file:
        if os.path.getsize(file_path) == 0:
            return 0
        file.seek(0, 2)
        full_length = file.tell() + 1

        if full_length % LINE_LENGTH != 0:
            print(message)
            return None
    return 1


def lines_counter(file_path):
    """ I return the amount of lines in database """

    LINE_LENGTH = struct.calcsize("38s23s10s1b")
    with open(file_path, "rb") as file:
        file.seek(0, 2)
        full_size = file.tell()
        file.seek(0, 0)
        count_lines = full_size // LINE_LENGTH
    return count_lines


def menu(file_path):
    """ I show User's menu """

    if file_path is not None:
        file_state = "успешно установлен"
    else:
        file_state = "не установлен"

    MENU_WIDTH = 50
    print(
        "\n"
        "|" + "-" * MENU_WIDTH + "|" + "\n"
        "|" + f"{'Создайте свой учебный To-Do лист':^{MENU_WIDTH}}" + "|" + "\n"
        "|" + "-" * MENU_WIDTH + "|" + "\n"
        "|" + f"{'    1. Выбрать файл для работы c планнером.':^{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       2. Инициализировать планнер.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       3. Показать список задач.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       4. Добавить запись по номеру строки.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       5. Удалить запись по номеру строки.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       6. Поиск задачи типу работы.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       7. Поиск задачи по предмету и приоритету.':<{MENU_WIDTH}}" + "|" + "\n"                                                                           
        "|" + f"{'       0. Завершение работы':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + " " * MENU_WIDTH + "|" + "\n"
        "|" + f"{f'      (*) Файл для работы {file_state}.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + "-" * MENU_WIDTH + "|" + "\n"
    )
    users_choice = check.get_exact_integer("Введите действие: ", 0, 7)

    return users_choice


def shut_down():
    global power_on
    power_on = False
    print(">> Программа успешно завершена.")


def get_file():
    """ I'm asking User for file path input """

    file_path = None
    while file_path is None:
        print("\n>> Текущая директория:")
        os.system("pwd")
        print("\n>> Название файла не должно содержать пробелов.")
        file_path = check.get_solid_input("Укажите путь к файлу, в котором хотите создать планнер: ")
        file_path = check_file(file_path, "(!) Ошибка: Данного файла не существует, либо он не может быть создан. "
                                          "Повторите ввод.")
    return file_path


def init_db(file_path):
    """
    This function clears out everything in picked file. Note, that if there's already a BD, it will ask User
    to approve initializing in order to prevent database being deleted.
    """

    does_exist = check_file(file_path, "(!) Перед созданием планнера установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return

    does_database = check_database(file_path, "")
    if does_database == 1:
        print("(!) Данный файл уже содержит планнер. Повторная инициализация сотрет все содержимое.")
        rewrite = check.get_exact_strings("Перезаписать файл (да/нет)? - ", "да", "нет")

    if does_database == 1 and rewrite == "да" or does_database is None or does_database == 0:
        with open(file_path, "wb") as file:
            file.close()
        file_name = file_path.rsplit("/", 1)[-1]
        print(f">> Планнер успешно инициализирован в файле с именем '{file_name}'.")
    else:
        return


def get_db(file_path):
    does_exist = check_file(file_path, "(!) Перед работой с планнером установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return

    does_database = check_database(file_path, "(!) Выбранный вами файл не содержит планнера.")
    if does_database == 0:
        print("Записи отсутствуют.\n(!) Добавить запись можно с помощью пункта '4' меню.")
        return

    # Print the heading
    TABLE_WIDTH = 103
    print(
    "\n"
    "|" + "-" * TABLE_WIDTH + "|" + "\n"
    "|" + f"{'Мои предстоящие работы.':^{TABLE_WIDTH}}" + "|" + "\n"
    "|" + "-" * TABLE_WIDTH + "|" + "\n"
    "|{:^5}|{:^40}|{:^25}|{:^24}|{:^5}|".format("№", "Предмет", "Тип работы", "Дэдлайн", "!") + "\n"
    "|" + "-" * TABLE_WIDTH + "|" + "\n"
    "|" + "-" * TABLE_WIDTH + "|"
    )

    # Reading file "token-by-token", decoding each token and printing it
    line_unpacking_format = "38s23s10s1b"
    LINE_LENGTH = struct.calcsize("38s23s10s1b")
    count_lines = lines_counter(file_path)
    with open(file_path, "rb") as file:
        current_line = 1

        for line in range(count_lines):
            line = file.read(LINE_LENGTH)
            line = list(struct.unpack(line_unpacking_format, line))

            # By that time we have line being decoded and stored in list.
            for i in range(len(line)):
                if i == 3:
                    pass
                else:
                    line[i] = line[i].decode("utf-8").replace("\x00", "")
            line.insert(0, current_line)
            print("|{:^5}|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line]))
            print("|" + "-" * TABLE_WIDTH + "|")
            current_line += 1


def add_line(file_path):
    does_exist = check_file(file_path, "(!) Перед созданием планнера установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return

    does_database = check_database(file_path, "(!) Перед добавлением записи инициализируйте планнер (Пункт '2' "
                                              "меню).\nДанное действие удалит информацию из файла.")
    if does_database is None:
        return

    count_lines = lines_counter(file_path)
    print(f">> Текущее количество записей в планнере: {count_lines}")
    if count_lines == 0:
        print(">> Пока что в планнере отсутствуют какие-либо записи. Добавьте первую строчку: ")
        line_to_add = 1
    else:
        add_range = f"от 1 до {count_lines + 1}"
        line_to_add = check.get_exact_integer(f"Укажите номер позиции, на которую вы хотите вставить строку: ({add_range}): ", 1, count_lines + 1)

    # Asking User to fulfill the fields.
    subject = check.get_fixed_input("Укажите название учебной дисциплины: ", 19)
    task = check.get_fixed_input("Укажите тип работы: ", 10)
    deadline = check.get_date("Укажите дэдлайн в формате ДД.ММ.ГГГГ: ")
    priority = int(check.get_exact_strings("Укажите приоритет 1 - 3: ", 1, 2, 3))

    # Packing data into bytes and structures
    subject_packed = struct.pack("38s", subject.encode("utf-8"))
    type_packed = struct.pack("23s", task.encode("utf-8"))
    deadline_packed = struct.pack("10s", deadline.encode("utf-8"))
    priority_packed = struct.pack("1b", priority)

    LINE_LENGTH = struct.calcsize("38s23s10s1b")
    # Writing packed data into file
    wall = LINE_LENGTH * (line_to_add - 1)
    swaps = count_lines - line_to_add + 1
    with open(file_path, "rb+") as file:
        for i in range(1, swaps + 1):
            file.seek(LINE_LENGTH * (count_lines - i), 0)
            buffer = file.read(LINE_LENGTH)
            file.write(buffer)

        file.seek(wall, 0)
        # Writing data
        file.write(subject_packed)
        file.write(type_packed)
        file.write(deadline_packed)
        file.write(priority_packed)


def delete_line(file_path):
    does_exist = check_file(file_path, "(!) Перед работой с планнером установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return

    does_database = check_database(file_path, "(!) Выбранный вами файл не содержит планнера.")
    if does_database == 0:
        print("Записи отсутствуют.\n(!) Добавить запись можно с помощью пункта '4' меню.")
        return

    count_lines = lines_counter(file_path)
    print(f">> Текущее количество записей в планнере: {count_lines}")
    if count_lines == 1:
        delete_range = 1
    else:
        delete_range = f"от 1 до {count_lines}"
    line_to_delete = check.get_exact_integer(f"Укажите номер строки, которую хотите удалить ({delete_range}): ", 1, count_lines) - 1

    with open(file_path, "rb") as file:
        file.seek(0, 2)
        full_size = file.tell()
    LINE_LENGTH = struct.calcsize("38s23s10s1b")
    wall = LINE_LENGTH * line_to_delete

    with open(file_path, "rb+") as file:

        while wall < full_size:
            file.seek(wall + LINE_LENGTH)
            buffer = file.read(LINE_LENGTH)
            file.seek(wall)
            file.write(buffer)
            wall += LINE_LENGTH
        file.truncate(full_size - LINE_LENGTH)


def find_by_task_type(file_path):
    does_exist = check_file(file_path, "(!) Перед работой с планнером установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return
    does_database = check_database(file_path, "(!) Выбранный вами файл не содержит планнера.")
    if does_database == 0:
        print("Записи отсутствуют.\n(!) Добавить запись можно с помощью пункта '3' меню.")
        return

    is_hooked = False
    hook = input("Задачи какого типа вас интересуют? - ")

    # Reading file "token-by-token", decoding each token and printing it
    line_unpacking_format = "38s23s10s1b"
    LINE_LENGTH = struct.calcsize("38s23s10s1b")
    TABLE_WIDTH = 103
    count_lines = lines_counter(file_path)
    with open(file_path, "rb") as file:
        current_line = 1

        for line in range(count_lines):
            line = file.read(LINE_LENGTH)
            line = list(struct.unpack(line_unpacking_format, line))

            # By that time we have line being decoded and stored in list.
            for i in range(len(line)):
                if i == 3:
                    line[i] = line[i]
                else:
                    line[i] = line[i].decode("utf-8").replace("\x00", "")
            line.insert(0, current_line)

            if hook in line[2]:
                if not is_hooked:
                    print("|" + "-" * TABLE_WIDTH + "|")
                    is_hooked = True
                print("|{:^5}|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line]))
                current_line += 1
        if is_hooked:
            print("|" + "-" * TABLE_WIDTH + "|")
        else:
            print(f"Ура! Работ типа '{hook}' не предвидется!")

def find_by_priority_and_subject(file_path):
    does_exist = check_file(file_path, "(!) Перед работой с планнером установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return
    does_database = check_database(file_path, "(!) Выбранный вами файл не содержит планнера.")
    if does_database == 0:
        print("Записи отсутствуют.\n(!) Добавить запись можно с помощью пункта '3' меню.")
        return

    is_hooked = False
    hook_1 = input("Задачи по какому предмету вас интересуют? - ")
    hook_2 = input(f"Задачи какого приоритета вас интересуют по предмету '{hook_1}'? - ")

    # Reading file "token-by-token", decoding each token and printing it
    line_unpacking_format = "38s23s10s1b"
    LINE_LENGTH = struct.calcsize("38s23s10s1b")
    TABLE_WIDTH = 103
    count_lines = lines_counter(file_path)
    with open(file_path, "rb") as file:
        current_line = 1

        for line in range(count_lines):
            line = file.read(LINE_LENGTH)
            line = list(struct.unpack(line_unpacking_format, line))

            # By that time we have line being decoded and stored in list.
            for i in range(len(line)):
                if i == 3:
                    line[i] = line[i]
                else:
                    line[i] = line[i].decode("utf-8").replace("\x00", "")
            line.insert(0, current_line)

            if hook_1 in line[1] and hook_2 in line[-1]:
                if not is_hooked:
                    print("|" + "-" * TABLE_WIDTH + "|")
                    is_hooked = True
                print("|{:^5}|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line]))
                current_line += 1
        if is_hooked:
            print("|" + "-" * TABLE_WIDTH + "|")
        else:
            print(f"Ура! Работ по предмету '{hook_1}' с приоритетом '{hook_2}' не предвидется!")


if __name__ == "__main__":
    power_on = True
    file_path = None

    while power_on:
        users_choice = menu(file_path)

        if users_choice == 0:
            shut_down()
        elif users_choice == 1:
            file_path = get_file()
        elif users_choice == 2:
            init_db(file_path)
        elif users_choice == 3:
            get_db(file_path)
        elif users_choice == 4:
            add_line(file_path)
        elif users_choice == 5:
            delete_line(file_path)
        elif users_choice == 6:
            find_by_task_type(file_path)
        elif users_choice == 7:
            find_by_priority_and_subject(file_path)



