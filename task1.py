# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
nums = []
for i in range(random.randint(5, 15)):
    nums.append(random.randint(1, 10))

x = int(random.randint(1, 14))

count = 0
for num in nums:
    if num == x:
        count += 1

print(f'В массиве:\n{nums} число {x} встречается {count} раз(а)')