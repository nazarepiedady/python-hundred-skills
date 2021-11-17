number_list = []

for number in range(1000, 1500):
    if (number % 7 == 0) and (number % 5 != 0):
        number_list.append(str(number))

raw_tuple = ', '.join(number_list)

print(raw_tuple)
