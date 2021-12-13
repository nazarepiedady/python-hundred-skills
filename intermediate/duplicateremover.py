def remove_duplicates(received_list: list) -> list:
    new_list = []

    for item in received_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

numbers_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

print(remove_duplicates(numbers_list))
