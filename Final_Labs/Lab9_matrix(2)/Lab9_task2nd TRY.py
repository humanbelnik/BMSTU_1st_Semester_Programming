nums = []
m = int(input("Введите ранг квадратной матрицы (Нечетный): "))

for i in range(m):
    nums.append(list(map(int,input(f">> Введите {m} элементов {i + 1}-й строки через пробел: ").split(" "))))
for line in nums:
    print(*line)

# Counting sum of dial elements
mid = m//2
mid_elem = nums[mid][mid]
dial_sum = 0
sum = 0
for i in range(m):
    dial_sum += nums[i][i]
for i in range(m):
    dial_sum += nums[i][m - 1 - i]
dial_sum -= mid_elem

for i in range(mid + 1, m, 1):
    sum += nums[mid][i]
sum += dial_sum

for i in range(m):
    for j in range(i + 1, m):
        if i + j >= mid + 1:
            continue
        nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
for i in range(m):
    for j in range(m):
        if j > i:
            sum += nums[i][j]
sum -= m//2
print("Искомая сумма: ", sum)








