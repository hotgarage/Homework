# Знайти суму елементів з парними індексами, помножити на останній

# Приклад 1: [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
nums = [0, 1, 7, 2, 4, 8]
if len(nums) == 0:                  # якщо список порожній
    result = 0                       # результат одразу 0
else:
    even_sum = 0                     # змінна для суми елементів з парними індексами
    for i in range(0, len(nums), 2):  # i = 0, 2, 4 ... (тільки парні індекси)
        even_sum += nums[i]           # додаємо nums[0], потім nums[2], потім nums[4]...
    result = even_sum * nums[-1]     # множимо суму на останній елемент
print(result)

# Приклад 2: [1, 3, 5] => 30
nums = [1, 3, 5]
if len(nums) == 0:
    result = 0
else:
    even_sum = 0
    for i in range(0, len(nums), 2):
        even_sum += nums[i]
    result = even_sum * nums[-1]
print(result)

# Приклад 3: [6] => 36
nums = [6]
if len(nums) == 0:
    result = 0
else:
    even_sum = 0
    for i in range(0, len(nums), 2):
        even_sum += nums[i]
    result = even_sum * nums[-1]
print(result)

# Приклад 4: [] => 0
nums = []
if len(nums) == 0:
    result = 0
else:
    even_sum = 0
    for i in range(0, len(nums), 2):
        even_sum += nums[i]
    result = even_sum * nums[-1]
print(result)