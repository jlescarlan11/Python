"""
list comprehension =    a way to create a new list with less syntax
                        can mimic certain lambda functions, easier to read
                        list = [expression for item in iterable]
                        list = [expression for item in iterable if conditional]
                        list = [expression if/else for item in iterable]
"""

# Original list of students' scores
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# Using list comprehension to create a list of boolean values (True if passed, False if failed)
# This uses the condition x >= 60 to determine passing or failing
# Result: [True, True, True, True, True, False, False, False, False]
# Note: This is not the final desired output, just an intermediate step
# passed_students = [x >= 60 for x in students]

# Using the filter function with a lambda function to get a list of scores where the students passed (score >= 60)
# Result: [100, 90, 80, 70, 60]
# Note: This is an alternative approach using filter and lambda
passed_students = list(filter(lambda x: x >= 60, students))

# Using list comprehension to directly create a list of scores where the students passed (score >= 60)
# Result: [100, 90, 80, 70, 60]
# Note: This is a concise and readable way to achieve the same result as the filter approach
passed_students = [i for i in students if i >= 60]

# Using list comprehension with conditional expression to create a list with grades ("FAILED" if < 60, score otherwise)
# Result: ['100', '90', '80', '70', '60', 'FAILED', 'FAILED', 'FAILED', 'FAILED']
# Note: This shows the use of if/else in list comprehension
passed_students = [i if i >= 60 else "FAILED" for i in students]

# Printing the final list of passed students
print(passed_students)
