#  Перемістити останній елемент списку на початок

# [12, 3, 4, 10] => [10, 12, 3, 4]
nums = [12, 3, 4, 10]
if len(nums) > 0:           # якщо список не порожній
    nums.insert(0, nums[-1])  # 1) вставити останній елемент на початок
    nums.pop()                # 2) видалити останній (він там тепер дублюється)
print(nums)

# [1] => [1]
nums = [1]
if len(nums) > 0:
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)

# [] => []
nums = []
if len(nums) > 0:
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)

# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]
nums = [12, 3, 4, 10, 8]
if len(nums) > 0:
    nums.insert(0, nums[-1])
    nums.pop()
print(nums)