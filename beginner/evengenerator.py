def even_number_generator(number):
    loop_limit_number = 0

    while loop_limit_number <= number:
        if loop_limit_number % 2 == 0:
            yield loop_limit_number
        loop_limit_number += 1


numbers_list = []

received_number = int(input('insert a number: '))

for number in even_number_generator(received_number):
    numbers_list.append(str(number))


print(','.join(numbers_list))
