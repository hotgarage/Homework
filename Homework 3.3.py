# Розділити один список на два списки

# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
nums = [1, 2, 3, 4, 5, 6]
middle_index = len(nums) // 2    # знаходимо "середину" — ділимо довжину навпіл
if len(nums) % 2 != 0:            # якщо довжина НЕПАРНА (є залишок при діленні на 2)
    middle_index += 1              # зсуваємо середину на 1 вправо (щоб перша частина була більша)
part1 = nums[:middle_index]       # беремо все від початку ДО середини
part2 = nums[middle_index:]       # беремо все від середини ДО кінця
print([part1, part2])              # збираємо список із двох списків і друкуємо

# [1, 2, 3] => [[1, 2], [3]]
nums = [1, 2, 3]
middle_index = len(nums) // 2
if len(nums) % 2 != 0:
    middle_index += 1
part1 = nums[:middle_index]
part2 = nums[middle_index:]
print([part1, part2])

#  [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
nums = [1, 2, 3, 4, 5]
middle_index = len(nums) // 2
if len(nums) % 2 != 0:
    middle_index += 1
part1 = nums[:middle_index]
part2 = nums[middle_index:]
print([part1, part2])

#  [1] => [[1], []]
nums = [1]
middle_index = len(nums) // 2
if len(nums) % 2 != 0:
    middle_index += 1
part1 = nums[:middle_index]
part2 = nums[middle_index:]
print([part1, part2])

#  [] => [[], []]
nums = []
middle_index = len(nums) // 2
if len(nums) % 2 != 0:
    middle_index += 1
part1 = nums[:middle_index]
part2 = nums[middle_index:]
print([part1, part2])