# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy

m, n = map(int, input().split())

my_array = numpy.array(list(map(int, input().split())))
reshaped_array = numpy.reshape(my_array, (m, n))

result = numpy.prod(reshaped_array)
print(result)
