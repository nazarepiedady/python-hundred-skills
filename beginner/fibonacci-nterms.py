nterm = int(input('Enter value of n: '))

first_number = 0
second_number = 1

numeric_counter = 0

if nterm <= 0:
    print('Please enter a positive integer')
elif nterm == 1:
    print('Fibonacci sequence upto', nterm, ':', first_number)
else:
    print('Fibonacci sequence upto', nterm, ':')
    while numeric_counter < nterm:
        print(first_number, end=' , ')
        nth = first_number + second_number
        first_number = second_number
        second_number = nth
        numeric_counter += 1
