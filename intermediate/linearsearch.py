def linear_search(list_to_search, item):
    position = 0
    found = False

    while position < len(list_to_search) and not found:
        if list_to_search[position] == item:
            found = True
        else:
            position = position + 1

    return (found, position)


list_of_numbers = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]


print(linear_search(list_of_numbers, 31))
