values_comma_separated = input('Enter comma-separated numbers: ')

list_number = list()

for number_string in values_comma_separated.split(','):
    list_number.append(number_string.strip())

tuple_number = tuple(list_number)

print(list_number)
print(tuple_number)
