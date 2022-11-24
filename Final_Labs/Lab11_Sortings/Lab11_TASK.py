"""
Защита ЛР №11
Сортировка вставками
"""


def get_positive_int(message):
    value = None
    while value is None:
        value = input(message)
        try:
            value = float(value)
        except ValueError:
            print("Размер массива: целое число. Повторите ввод.")
            value = None
            continue
        if value < 0:
            print("Размер массива неотрицателен. Повторите ввод.")
        if value == 0:
            print("Вы ввели пустой массив. Сортировка не определена. Повторите ввод.")
            value = None
    return int(value)


def get_number(message):
    value = None

    while value is None:
        value = input(message)

        try:
            value = float(value)
        except ValueError:
            print("Размер массива: целое число. Повторите ввод.")
            value = None
            continue

    if float(value) == int(value):
        return int(value)
    else:
        return value


def insert_sort(nums):
    for i in range(1, len(nums)):
        element = nums[i]
        j = i - 1  # Previous element's index in ALREADY sorted section
        while j >= 0 and nums[j] > element:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = element

    return nums


# Main
nums = []
n = get_positive_int("Введите размер массива: ")
for i in range(n):
    element = get_number(f"Введите {i + 1}-й элемент массива: ")
    nums.append(element)
print("Вы ввели массив:\n", *nums)

nums_sorted = insert_sort(nums)
print("Ваш массив успешно отсортирован:\n", *nums_sorted)
