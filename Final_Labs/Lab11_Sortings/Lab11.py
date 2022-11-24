"""
Беляев Никита, ИУ7-11б
Лабораторная работа №11: "Исследование методов сортировки"

Метод:
Шейкер-сортировка.

Задание:
1. Отсортировать введнный пользователем массив.
2. Для взять по три массива (Отсортированный, Рандомный и Отсортированный в обратном порядке)
   трех различных размеров и отсортировать их. Вывести таблицу, отражающую время выполнения алгоритма и
   количество перестановок для каждого из 9-ти случаев.
"""

import random as r
import time as t
import CheckValues as check


def get_sorted_array(size):
    array = [i for i in range(size)]
    return array


def get_random_array(size):
    array = [r.randint(-size, size) for i in range(size)]
    return array


def get_reversed_array(size):
    array = [i for i in range(size - 1, -1, -1)]
    return array


def shaker_sort(nums, isUser=False):

    # Variables for measuring swaps & time
    swaps = 0
    start_time = 0
    end_time = 0

    # Variables for shaker sort
    left_wall = 0
    right_wall = len(nums) - 1
    sorted = False

    # Iterating back end forth until array is fully sorted
    start_time = t.monotonic_ns()
    while not sorted:
        sorted = True

        # If there will be no swaps, array is already sorted -> we'll break
        for i in range(left_wall, right_wall):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swaps += 1
                sorted = False

        if sorted:
            break

        sorted = True
        right_wall -= 1

        for i in range(right_wall, left_wall - 1, -1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swaps += 1
                sorted = False

        left_wall += 1
    end_time = t.monotonic_ns()

    if isUser:
        return nums
    else:
        time = end_time - start_time
        return time, swaps


# Main

# Working with User's array
nums = []
n = check.get_positive_integer("Введите размер целочисленного массива: ", message="Массив пуст. Сортировка не определена.")

for i in range(n):
    nums.append(check.get_integer(f"Введите {i + 1}-й элемент массива: ", message="Элемент"))
print("\n>> Вы ввели целочисленный массив:\n", *nums)

nums_sorted = shaker_sort(nums, isUser=True)
print("\n>> Ваш массив успешно отсортирован по возрастанию:\n", *nums_sorted, "\n")


# Working with different arrays (Table)

size_1 = check.get_positive_integer("Введите размерность для первого эксперимента: ", message="Массив пуст. Соритровка не определена.")
size_2 = check.get_positive_integer("Введите размерность для второго эксперимента: ", message="Массив пуст. Сортировка не определена.")
size_3 = check.get_positive_integer("Введите размерность для третьего эксперимента: ", message="Массив пуст. Сортировка не определена.")


# Sorting arrays with their time and swaps measured.

# First experiment
sorted_time_1, sorted_swaps_1 = shaker_sort(get_sorted_array(size_1))
random_time_1, random_swaps_1 = shaker_sort(get_random_array(size_1))
reversed_time_1, reversed_swaps_1 = shaker_sort(get_reversed_array(size_1))


# Second experiment
sorted_time_2, sorted_swaps_2 = shaker_sort(get_sorted_array(size_2))
random_time_2, random_swaps_2 = shaker_sort(get_random_array(size_2))
reversed_time_2, reversed_swaps_2 = shaker_sort(get_reversed_array(size_2))

# Third experiment
sorted_time_3, sorted_swaps_3 = shaker_sort(get_sorted_array(size_3))
random_time_3, random_swaps_3 = shaker_sort(get_random_array(size_3))
reversed_time_3, reversed_swaps_3 = shaker_sort(get_reversed_array(size_3))

data_1 = (shaker_sort(get_random_array(size_1)))
print(">> Data for the 1st experiment:\n", f"Time: {data_1[0]}\nSwaps: {data_1[1]}")


# Table
print("-" * 128)
print("|" + "|{:^28}|".format("Размерность") + "|" + "{:^30.5g}||".format(size_1) + "{:^30.5g}||".format(size_2) + "{:^30.5g}||".format(size_3))
print("-" * 128)
print("|" + "|{:^28}|".format("Параметр") + "|" + ("{:^15}|{:^14}||".format("Время (нс) ", "Перестановки")) * 3)
print("-" * 128)

print("|" + "|{:^28}|".format("Упорядоченный список") + "|" + "{:^15.5g}|".format(sorted_time_1) + "{:^14.7g}||".format(sorted_swaps_1)
      + "{:^15.5g}|".format(sorted_time_2) + "{:^14.7g}||".format(sorted_swaps_2)
      + "{:^15.5g}|".format(sorted_time_3) + "{:^14.7g}||".format(sorted_swaps_3)
      )
print("-" * 128)
print("|" + "|{:^28}|".format("Случайный список") + "|" + "{:^15.5g}|".format(random_time_1) + "{:^14.7g}||".format(random_swaps_1)
      + "{:^15.5g}|".format(random_time_2) + "{:^14.7g}||".format(random_swaps_2)
      + "{:^15.5g}|".format(random_time_3) + "{:^14.7g}||".format(random_swaps_3)
      )
print("-" * 128)
print("|" + "|{:^28}|".format("Развернутый список") + "|" + "{:^15.5g}|".format(reversed_time_1) + "{:^14.7g}||".format(reversed_swaps_1)
      + "{:^15.5g}|".format(reversed_time_2) + "{:^14.7g}||".format(reversed_swaps_2)
      + "{:^15.5g}|".format(reversed_time_3) + "{:^14.7g}||".format(reversed_swaps_3)
      )
print("-" * 128)















