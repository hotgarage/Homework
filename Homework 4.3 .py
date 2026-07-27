# Список із 3 елементів

# Приклад 1: [1, 2, 3, 4, 5, 6, 7, 9] -> [1, 3, 7]
nums = [1, 2, 3, 4, 5, 6, 7, 9]
result = [nums[0], nums[2], nums[-2]]   # перший + третій + другий з кінця
print(result)

# Приклад 2: [1, 1, 2, 1] -> [1, 2, 1]
nums = [1, 1, 2, 1]
result = [nums[0], nums[2], nums[-1]]
print(result)

# Приклад 3: [6, 3, 7] -> [6, 7, 3]
nums = [6, 3, 7]
result = [nums[0], nums[2], nums[-2]]
print(result)