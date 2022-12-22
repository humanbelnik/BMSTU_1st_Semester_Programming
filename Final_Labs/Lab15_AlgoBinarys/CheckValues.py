#  This module contains functions for checking if inputted values are incorrect.
#  Each function takes two necessary arguments:
#      1. String "intro" - input introduction in order to make program User Friendly
#      2. Value
#     *3. String "message" - name of the value to show when User made a mistake and wants to input it again

import re

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

        if value > 2_147_483_647 or value < -2_147_483_648:
            print("(!!!) Вы ввели число, которое не входит в диапазон 4-х байт. Пожалуйста, повторите ввод.")
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
            print(f"(!!!) {message} - положительное целое число. Повторите ввод.")
            value = None
            continue

        if int(value) != float(value) or value <= 0:
            print(f"(!!!) {message} - положительное число. Повторите ввод.")
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
    strings = [str(x) for x in strings]
    while string is None:
        string = input(intro)

        try:
            string = str(string)
        except ValueError:
            print("(!) Повторите ввод!")
            string = None
            continue
        if string not in strings:
            print("(!) Повторите ввод!")
            string = None
            continue
    return string


def get_fixed_input(message, max_length, sep="0"):
    word = None
    while word is None:
        word = input(message)
        if word == "":
            print("Вы не заполнили поле. Повторите ввод.")
            word = None
            continue
        if len(word) > max_length:
            print(f"(!) Данное поле позволяет ввести максимум {max_length} символов",
                  f"Вы ввели {len(word)} символов. Повторите ввод.")
            word = None
            continue
        for letter in word:
            if letter == sep: # or not letter.isalpha():
                print(f"Поле может содержать только буквы. Повторите ввод.")
                word = None
                continue
    return word

# "^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$"
def get_date(message):
    word = None
    while word is None:
        word = input(message)
        if re.match("^[0-3][0-9].[0-3][0-9].([0-9]{2})[0-9]{2}$", word) is None:
            print("Вы ввели некорректную дату. Повторите ввод.")
            word = None
            continue
    return word

#TEST
#get_exact_strings("", [1, 2 ,3])

def get_solid_input(intro):
    word = None
    while word is None:
        word = input(intro)
        if " " in word or word == "":
            print("Путь к файлу не должен содержать пробелов. Повторите ввод.")
            word = None
            continue
    return word
















