sentence = str(input('Enter a sentence: '))

counter_dictionary = {
    'UPPER CASE': 0,
    'LOWER CASE': 0
}

for character in sentence:
    if character.isupper():
        counter_dictionary['UPPER CASE'] += 1
    elif character.islower():
        counter_dictionary['LOWER CASE'] += 1
    else:
        pass

print('UPPER CASE', counter_dictionary['UPPER CASE'])
print('LOWER CASE', counter_dictionary['LOWER CASE'])
