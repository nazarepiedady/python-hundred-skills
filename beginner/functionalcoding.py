import functools


def function(number):
    return number % 2 != 0 and number % 3 != 0

function_result = list(filter(function, range(2, 25)))

print(function_result)

def cube(number):
    return number * number * number

cube_result = list(map(cube, range(1, 11)))

print(cube_result)

def add(first_number, second_number):
    return first_number + second_number

add_result = functools.reduce(add, range(1, 11))

print(add_result)
