# Type casting = convert the data type of a value to another data type.

x = 1 # int
y = 2.0 # float
z = '3' # str

print('Before type casting:')
print(x)
print(y)
print(z*3)

# This type cast y
x = float(x)
y = int(y)
z = int(z)

print()

print('After type casting:')
print(x)
print(y)
print(z*3)

"""
NOTE: We type cast when we need to concatinate a variable with another 
variable of different type.
"""