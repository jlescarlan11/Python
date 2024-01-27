"""
Higher Order Function = a function that either:
                        1. accepts a function as an argument
                            or
                        2. returns a function
                        (In python, functions are also treated as objects )
"""

# Higher Order Function Example:

# 1. Functions as Arguments

# Define two functions, 'loud' and 'quiet'
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

# Define a higher-order function 'hello' that takes a function as an argument
def hello(func):
    # Call the provided function with the argument "Hello"
    text = func("Hello")
    # Print the result
    print(text)

# Call 'hello' with the 'loud' and 'quiet' functions
hello(loud)
hello(quiet)

# 2. Functions as Return Values

# Define a function 'divisor' that takes a parameter 'x'
def divisor(x):
    # Define a nested function 'dividend' that takes a parameter 'y'
    def dividend(y):
        # Return the result of 'y / x'
        return y / x
    # Return the 'dividend' function (a function that takes 'y' and returns 'y / x')
    return dividend

# Call 'divisor' with an argument of 2, resulting in the 'dividend' function for division by 2
divide = divisor(2)

# Call 'divide' with an argument of 10, which effectively performs 10 / 2
print(divide(10))
