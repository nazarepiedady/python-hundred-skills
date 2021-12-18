import numpy

floating_values_array = numpy.arange(7)

print('Original array')
print(floating_values_array)

print(
    'First array elements raised to powers from second array, element-wise:'
)
print(numpy.power(floating_values_array, 3))

print('Element-wise absolute value:')
print(numpy.absolute(floating_values_array))
