#!/bin/python3

comma_values = input('Insert a comma-separeted numbers: ')

number_list = [
  str(int(number) ** 2) for number in comma_values.split(',') if (int(number) % 2 != 0)]


print(','.join(number_list))
