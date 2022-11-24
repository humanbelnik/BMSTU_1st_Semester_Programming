#  This module contains functions for checking if inputted values are incorrect.
#  Each function takes two necessary arguments:
#      1. String "intro" - input introduction in order to make program User Friendly
#      2. Value
#     *3. String "message" - name of the value to show when User made a mistake and wants to input it again

# Число
# Целое число
# Положительное целое
# Положительное дробное
# Неотрицательное целое
# Неотрицательное


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




def get_positive_float(intro, value, message="Входное значние"):
    value = input(intro)

    try:
        value = float(value)
    except ValueError:
        print(f"(!!!) {message} -  положительное число. Повторите ввод.")
        return None

    if value <= 0:
        print(f"(!!!) {message} - положительное число. Повторите ввод.")
        return None
    return value


def get_non_negative_float(intro, value, message="Входное значние"):
    value = input(intro)

    try:
        value = float(value)
    except ValueError:
        print(f"(!!!) {message} -  неотрицательное число. Повторите ввод.")
        return None

    if value < 0:
        print(f"(!!!) {message} - неотрицатнльное число. Повторите ввод.")
        return None
    return value







