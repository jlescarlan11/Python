"""
lambda function =   function written in 1 line using ambda keyword
                    accepts any number of arguments, but only one expression.
                    (think of it as a shortcut)
                    (useful if needed for a short period of  time, throw-away)

lambda  parameter:expression
"""

# Lambda function to double the value of a number
double = lambda x: x * 2

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y

# Lambda function to add three numbers
add = lambda x, y, z: x + y + z

# Lambda function to concatenate two strings
full_name = lambda first_name, last_name: first_name + ' ' + last_name

# Lambda function for age check (returns True if age is 18 or more, else False)
age_check = lambda age: True if age >= 18 else False

# Testing the lambda functions
print(double(5))               # Output: 10
print(multiply(2, 5))           # Output: 10
print(add(1, 2, 3))             # Output: 6
print(full_name('lest', 'blah'))# Output: lest blah
print(age_check(18))            # Output: True
