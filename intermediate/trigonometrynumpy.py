import numpy


print('sine: array of angles given in degrees')
print(numpy.sin(numpy.array((0., 30., 45., 60., 90.)) * numpy.pi / 180.))

print('cosine: array of angles given in degrees')
print(numpy.cos(numpy.array((0., 30., 45., 60., 90.)) * numpy.pi / 180.))

print('tangent: array of angles given in degrees')
print(numpy.tan(numpy.array((0., 30., 45., 60., 90.)) * numpy.pi / 180.))
