"""
filter() = creates a collection of elements from an iterable for which a function returns

firter(function, iterable)
"""

# Define a list of friends, where each element is a tuple containing a name and an age.
friends = [('Rachel', 19),
           ('Monica', 18),
           ('Phoebe', 17),
           ('Joey', 16),
           ('Chandler', 21),
           ('Ross', 20)]

# Define a lambda function 'age' that takes a data tuple and returns True if the age (index 1) is greater than or equal to 18.
age = lambda data: data[1] >= 18

# Use the filter() function to create a new list 'drinking_buddies' by filtering elements from 'friends' based on the 'age' function.
drinking_buddies = list(filter(age, friends))

# Iterate through the 'drinking_buddies' list and print each tuple (name and age).
for i in drinking_buddies:
    print(i)
