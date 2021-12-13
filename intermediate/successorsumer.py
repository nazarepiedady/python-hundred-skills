range_limit_number = int(input('insert a number: '))

summation = 0.0

for range_number in range(1, range_limit_number + 1):
    summation += float(float(range_number) / (range_number + 1))

print(summation)
