"""
Беляев Никита, ИУ7-11б
Лабораторная работа №13. "База данных в текстовом файле"

Задание:
С помощью меню организовать работу с текстовой базой данных на произвольную тематику.
"""

import os
import datetime
import CheckValues as check


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
        "|" + f"{'       2. Создать планнер.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       3. Добавить запись в планнер.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       4. Показать список задач.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       5. Поиск задачи по дэдлайну.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       6. Поиск задачи по предмету и приоритету.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + f"{'       0. Завершение работы':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + " " * MENU_WIDTH + "|" + "\n"
        "|" + f"{f'      (*) Файл для работы {file_state}.':<{MENU_WIDTH}}" + "|" + "\n"
        "|" + "-" * MENU_WIDTH + "|" + "\n"
    )
    users_choice = check.get_exact_integer("Введите действие: ", 0, 6)

    return users_choice


def shut_down():
    global power_on
    power_on = False
    print(">> Программа успешно завершена.")


# We use two-step check when calling any function for managing our database:
#    1. We check whether file path is correct or not
#    2. If file path is correct, we check what's inside. If it's empty or already contains DB, we can work with it.
#       if it filled with something else, we're asking user to init DB or choose different file.


def check_file(file_path, message):
    """ I check if the file path is correct """
    try:
        file = open(file_path, "a")
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
    with open(file_path, "r") as file:
        if os.path.getsize(file_path) == 0:
            file.close()
            return 0
        for line in file:
            if line.count("|") != 4:
                print(message)
                file.close()
                return None
    file.close()
    return 1


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
    does_exist = check_file(file_path, "(!) Перед созданием планнера установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return

    does_database = check_database(file_path, "")

    if does_database == 1:
        print("(!) Данный файл уже содержит планнер. Повторная инициализация сотрет все содержимое.")
        rewrite = check.get_exact_strings("Перезаписать файл (да/нет)? - ", "да", "нет")

    if does_database == 1 and rewrite == "да" or does_database is None or does_database == 0:
        with open(file_path, "w") as file:
            file.close()
        file_name = file_path.rsplit("/", 1)[-1]
        print(f">> Планнер успешно инициализирован в файле с именем '{file_name}'.")
    else:
        return


def add_line(file_path):

    # We check if the file_path is settled and what's inside a file if it's settled correctly.
    does_exist = check_file(file_path, "(!) Перед созданием планнера установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return
    does_database = check_database(file_path, "(!) Перед добавлением записи инициализируйте планнер (Пункт '2' "
                                              "меню).\nДанное действие удалит информацию из файла.")
    if does_database is None:
        return

    # Asking User to fulfill the fields.
    subject = check.get_fixed_input("Укажите название учебной дисциплины: ", 38)
    task_type = check.get_fixed_input("Укажите тип работы: ", 23)
    deadline = check.get_date("Укажите дэдлайн в формате ДД.ММ.ГГГГ: ")
    priorty = check.get_exact_strings("Укажите приоритет 1 - 3: ", 1, 2, 3)

    with open(file_path, "a") as file:
        file.write("{}|{}|{}|{}|\n".format(subject, task_type, deadline, priorty))
        file.close()


def get_db(file_path):

    # We check if the file_path is settled and what's inside a file if it's settled correctly.
    does_exist = check_file(file_path, "(!) Перед работой с планнером установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return
    does_database = check_database(file_path, "(!) Выбранный вами файл не содержит планнера.")
    if does_database == 0:
        print("Записи отсутствуют.\n(!) Добавить запись можно с помощью пункта '3' меню.")
        return

    # Print the heading
    TABLE_WIDTH = 97
    print(
    "\n"
    "|" + "-" * TABLE_WIDTH + "|" + "\n"
    "|" + f"{'Мои предстоящие работы.':^{TABLE_WIDTH}}" + "|" + "\n"
    "|" + "-" * TABLE_WIDTH + "|" + "\n"
    "|{:^40}|{:^25}|{:^24}|{:^5}|".format("Предмет", "Тип работы", "Дэдлайн", "!") + "\n"
    "|" + "-" * TABLE_WIDTH + "|" + "\n"
    "|" + "-" * TABLE_WIDTH + "|"
    )
    with open(file_path, "r") as file:
        for line in file:
            line_splitted = line.split("|")[:-1]
            print("|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line_splitted]))
            print("|" + "-" * TABLE_WIDTH + "|")
        file.close()


def find_by_meta_date(file_path, meta_hook):
    """ I find lines in DB using tags """
    current_time = datetime.datetime.now()
    current_day = current_time.day
    current_month = current_time.month
    current_year = current_time.year
    #current_weekday = current_time.weekday()
    days_by_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    is_hooked = False

    with open(file_path, "r") as file:
        for line in file:
            # Deconstructing the line in order to get access to day, month and year for current line
            line_splitted = line.split("|")[:-1]
            date_to_check = [int(x) for x in line_splitted[2].split(".")]
            day_to_check = date_to_check[0]
            month_to_check = date_to_check[1]
            year_to_check = date_to_check[2]

            # Leap year
            if current_year % 4 == 0:
                days_by_month[2] = 29

            if meta_hook == "сегодня" and day_to_check == current_day and \
                    month_to_check == current_month and year_to_check == current_year:
                if not is_hooked:
                    print("|" + "-" * 97 + "|")
                    is_hooked = True
                print("|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line_splitted]))

            elif meta_hook == "следующий месяц" and month_to_check == ((current_month + 1) // 12) and year_to_check == (
                    current_year + ((current_month + 1) % 12)):
                if not is_hooked:
                    print("|" + "-" * 97 + "|")
                    is_hooked = True
                print("|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line_splitted]))

            elif meta_hook == "завтра":
                if day_to_check == current_day + 1 and month_to_check == current_month and year_to_check == current_year:
                    if not is_hooked:
                        print("|" + "-" * 97 + "|")
                        is_hooked = True
                    print("|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line_splitted]))
                if day_to_check == 1 and current_day == days_by_month[current_month] and month_to_check == (
                        (current_month + 1) // 12) and year_to_check == (current_year + ((current_month + 1) % 12)):
                    if not is_hooked:
                        print("|" + "-" * 97 + "|")
                        is_hooked = True
                    print("|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line_splitted]))
        if is_hooked:
            print("|" + "-" * 97 + "|")
        file.close()
        return is_hooked


def find_by_date(file_path, META_SEARCH):

    # We check if the file_path is settled and what's inside a file if it's settled correctly.
    does_exist = check_file(file_path, "(!) Перед работой с планнером установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return
    does_database = check_database(file_path, "(!) Выбранный вами файл не содержит планнера.")
    if does_database == 0:
        print("Записи отсутствуют.\n(!) Добавить запись можно с помощью пункта '3' меню.")
        return

    meta_hooks = ["сегодня", "завтра", "следующий месяц"]
    is_hooked = False
    print(">> Для поиска конкретной даты используйте формат ДД.ММ.ГГГГ\n>> Также вы можете использовать тэги ("
          "сегодня/завтра/следующий месяц)")
    hook = input("Задачи на какое время вас интересуют? - ")

    # We search by tags if global META_SEARCH is True.
    if META_SEARCH:
        if hook in meta_hooks:
            is_hooked = find_by_meta_date(file_path, hook)

    # Searching by exact date
    with open(file_path, "r") as file:
        for line in file:
            line_splitted = line.split("|")
            if hook in line_splitted[-3]:
                if not is_hooked:
                    print("|" + "-" * 97 + "|")
                    is_hooked = True
                print("|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line_splitted]))
        file.close()
    if is_hooked:
        print("|" + "-" * 97 + "|")
    else:
        print(f"На {hook} ничего не запланировано.")


def find_by_priority_and_subject(file_path):

    # We check if the file_path is settled and what's inside a file if it's settled correctly.
    does_exist = check_file(file_path, "(!) Перед работой с планнером установите файл для работы (Пункт '1' меню).")
    if does_exist is None:
        return
    does_database = check_database(file_path, "(!) Выбранный вами файл не содержит планнера.")
    if does_database == 0:
        print("Записи отсутствуют.\n(!) Добавить запись можно с помощью пункта '3' меню.")
        return

    is_hooked = False
    hook_1 = input("Предстоящие мероприятия по какому предмету вы хотите найти? - ")
    hook_2 = input(f"Задачи какой важности вас интересуют по предмету '{hook_1}'? - ")
    with open(file_path, "r") as file:
        for line in file:
            line_splitted = line.split("|")
            if hook_2 in line_splitted[-2] and hook_1 in line_splitted[0]:
                if not is_hooked:
                    print("|" + "-" * 97 + "|")
                    is_hooked = True
                print("|{:^40}|{:^25}|{:^24}|{:^5}|".format(*[i for i in line_splitted]))
        file.close()
    if is_hooked:
        print("|" + "-" * 97 + "|")
    else:
        print(f"Работ, по предмету '{hook_1}' с приоритетом '{hook_2}' не предвидется.")


if __name__ == "__main__":
    power_on = True
    file_path = None
    META_SEARCH = True

    while power_on:
        users_choice = menu(file_path)

        if users_choice == 0:
            shut_down()
        elif users_choice == 1:
            file_path = get_file()
        elif users_choice == 2:
            init_db(file_path)
        elif users_choice == 3:
            add_line(file_path)
        elif users_choice == 4:
            get_db(file_path)
        elif users_choice == 5:
            find_by_date(file_path, META_SEARCH)
        elif users_choice == 6:
            find_by_priority_and_subject(file_path)




