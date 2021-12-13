import functools


numbers_list = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print(list(filter(lambda x: x % 3 == 0, numbers_list)))
print(list(map(lambda x: x * 2 + 15, numbers_list)))
print(functools.reduce(lambda x, y: x + y, numbers_list))
