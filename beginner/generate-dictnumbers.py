number = int(input('Enter a number: '))
dictionary = dict()

for index in range(1, number + 1):
    dictionary[index] = index * index

print(dictionary)
