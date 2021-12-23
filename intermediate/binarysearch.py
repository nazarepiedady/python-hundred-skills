import math


def binary_search(list_to_search, element):
    index = -1
    bottom = 0
    top = len(list_to_search) - 1
    
    while top >= bottom and index == -1:
        middle = int(math.floor((top + bottom) / 2.0))
        if list_to_search[middle] == element:
            index = middle
        elif list_to_search[middle] > element:
            top = middle - 1
        else:
            bottom = middle + 1

    return index


list_of_numbers = [2, 5, 7, 9, 11, 17, 222]

print(binary_search(list_of_numbers, 11))
print(binary_search(list_of_numbers, 12))
