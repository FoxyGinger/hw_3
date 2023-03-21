# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

nums = []
for i in range(random.randint(5, 15)):
    nums.append(random.randint(1, 10))

x = int(random.randint(1, 14))

closest_num = nums[0]
diff = abs(x - nums[0])
for num in nums:
    new_diff = abs(x - num)
    if new_diff < diff:
        closest_num = num
        diff = new_diff
        if diff == 0:
            break

print(f'В массиве:\n{nums} ближайшее к числу "{x}" число "{closest_num}"')
