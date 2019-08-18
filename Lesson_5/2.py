"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import defaultdict

nums = defaultdict(list)
input_nums = input('Введите два числа через прбел: ').split()

for num in input_nums:
    nums[num] = list(num)


sum = 0
mul = 1

for num in nums.keys():
    num = int(num, 16)
    sum += num
    mul *= num

sum_num = list(hex(sum).upper()[2:])
mul_num = list(hex(mul).upper()[2:])
print(*sum_num)
print(*mul_num)






