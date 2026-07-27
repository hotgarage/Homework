# Перемістити всі нулі в кінець списку

# Приклад 1: [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
nums = [0, 1, 0, 12, 3]
result = []                                  # 1) Створюємо порожній список для результату

for x in nums:                               # для кожного елемента x у списку nums
    if x != 0:                               # якщо x НЕ дорівнює 0
        result.append(x)                     # додаємо його в result

for x in nums:                               # знову йдемо по всьому nums
    if x == 0:                               # якщо x дорівнює 0
        result.append(x)                     # додаємо його в result (в кінець)
print(result)

# Приклад 2: [0] -> [0]
nums = [0]
result = []
for x in nums:
    if x != 0:
        result.append(x)
for x in nums:
    if x == 0:
        result.append(x)
print(result)

# Приклад 3: [1, 0, 13, 0, 0, 5] -> [1, 13, 5, 0, 0, 0]
nums = [1, 0, 13, 0, 0, 5]
result = []
for x in nums:
    if x != 0:
        result.append(x)
for x in nums:
    if x == 0:
        result.append(x)
print(result)

# Приклад 4: [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]
nums = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
result = []
for x in nums:
    if x != 0:
        result.append(x)
for x in nums:
    if x == 0:
        result.append(x)
print(result)