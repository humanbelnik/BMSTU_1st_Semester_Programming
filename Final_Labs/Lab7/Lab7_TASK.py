'''
Защита: Из целочисленного списка удалить все простые числа
'''

# Input
nums = []
n = int(input("Введите количество элементов в массиве: "))

for i in range(n):
    nums.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
print('Вы ввели массив: ', *nums)

# Del all prime nums
for i in range(len(nums) - 1, -1, -1):
    is_prime = True
    if nums[i] < 0 or nums[i] == 0:
        is_prime = False
        break
    for j in range(2, nums[i]):
        if nums[i] % j == 0:
            is_prime = False  # Нашли не простое число, его необходимо оставить.
            break
    if is_prime:  # Если число простое, его необходимо удалить
        for j in range(i, len(nums) - 1):
            nums[j] = nums[j + 1]
        del nums[len(nums) - 1]
print('Из массива удалены все простые числа:', *nums)



