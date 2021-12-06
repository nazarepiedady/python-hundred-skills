import random


roll_again = 'yes'

def print_software_header():
    print('Rolling the dices...')
    print('The values are...')

def roll_dice(min_value = 1, max_value = 6):
    return random.randint(min_value, max_value)

while roll_again == 'yes' or roll_again == 'y':
    print_software_header()
    print(roll_dice(), end=', ')
    print(roll_dice())
    roll_again = str(input('Roll the dices again?\na: ')).lower()
