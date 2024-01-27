"""
reduce =    apply a function to an iterable and reduce it to a single cumulative value.
            performs function on first two elements and repeats process until 1 value remains

reduce(function, iterable)
"""

# Import the functools module, which contains the reduce function
import functools

# Define a list of letters
letters = ['H', 'E', 'L', 'L', 'O']

# Use the reduce function to concatenate the letters into a single word
word = functools.reduce(lambda x, y: x + y, letters)
print(word)

# Define a list of factorial numbers
factorial = [5, 4, 3, 2, 1]

# Use the reduce function to calculate the factorial of the numbers
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
