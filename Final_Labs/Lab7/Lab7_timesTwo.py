'''
Беляев Никита ИУ7-11б
Лабораторная работа №7.

Задание:
После каждого элемента целочисленного списка, кратного трем, вставить его удвоеннное значение.
'''

print('Программа: После каждого элемента целочисленного списка, кратного трем, вставить его удвоеннное значение.')
nums = []
n = int(input('Введите количество элементов в списке: '))
counter = 0  # I store the amount of numbers which are divided by 3.

for i in range(n):
    nums.append(int(input(f'Введите {i + 1}-й элемент списка: ')))
    if nums[i] % 3 == 0:
        counter += 1
print('Вы ввели список:', *nums)

slots = [None for i in range(len(nums) + counter)]
nums += slots

# Algo
current = n
end = len(nums)
i = 0
while current < end:
    nums[current] = nums[i]
    if nums[i] % 3 != 0:  # Bad number
        current += 1
    else:
        nums[current + 1] = nums[i] * 2
        current += 2
    i += 1
nums = nums[n:]

print('Ваш список отредактирован:', *nums)