#  This module contains functions for checking if inputted values are incorrect.
#  Each function takes two necessary arguments:
#      1. String "intro" - input introduction in order to make program User Friendly
#      2. Value
#     *3. String "message" - name of the value to show when User made a mistake and wants to input it again


def get_integer(prompt, message="Входное значение"):
    value = None

    while value is None:
        value = input(prompt)
        try:
            value = float(value)
        except ValueError:
            print(f"(!!!) {message} - целое число. Повторите ввод.")
            value = None
            continue

        if int(value) != float(value):
            print(f"(!!!) {message} - целое число. Повторите ввод.")
            value = None
            continue

    return int(value)


def get_non_negative_integer(intro, message="Входное значние"):
    value = None

    while value is None:
        value = input(intro)
        try:
            value = float(value)
        except ValueError:
            print(f"(!!!) {message} - неотрицательное целое число. Повторите ввод.")
            value = None
            continue

        if int(value) != float(value) or value < 0:
            print(f"(!!!) {message} -  неотрицательное целое число. Повторите ввод.")
            value = None
            continue

    return int(value)


def get_positive_integer(intro, message="Входное значние"):
    value = None

    while value is None:
        value = input(intro)
        try:
            value = float(value)
        except ValueError:
            print(f"(!!!) {message} - неотрицательное целое число. Повторите ввод.")
            value = None
            continue

        if int(value) != float(value) or value <= 0:
            print(f"(!!!) {message} Повторите ввод.")
            value = None
            continue

    return int(value)


def get_exact_integer(intro, start, end):
    value = None
    nums = [x for x in range(start, end + 1)]

    while value is None:
        value = input(intro)
        try:
            value = float(value)
        except ValueError:
            print("(!) Данной функции не существует. Повторите ввод.")
            value = None
            continue
        if value != int(value) or value not in nums:
            print("(!) Данной функции не существует. Повторите ввод.")
            value = None
            continue
    return int(value)


def get_single_word(intro):
    word = None

    while word is None:
        word = input(intro)
        i = 0
        while i < len(word):
            if not word[i].isalnum():
                print("(!) Введите только одно слово.")
                word = None
                break
            i += 1

    return word

def get_exact_strings(intro, *strings):
    string = None

    while string is None:
        string = input(intro)
        if string not in strings:
            print("(!) Повторите ввод!")
            string = None
            continue
    return string















