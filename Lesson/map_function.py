"""
map() = applies a function to each item in an iterable (list, tuple, etc.)

map(function,iterable)
"""

# Define a list 'store' containing tuples, where each tuple represents an item and its price.
store = [('shirt', 20.00),
         ('pants', 25.00),
         ('jacket', 50.00),
         ('sock', 10.00)
         ]

# Define a lambda function 'to_euros' that takes a tuple (item, price) and converts the price to euros using a conversion factor of 0.82.
to_euros = lambda data: (data[0], data[1]*0.82)

# Use the map() function to apply the 'to_euros' function to each tuple in the 'store' list, creating a new list 'store_euros'.
store_euros = list(map(to_euros, store))

# Iterate through the 'store_euros' list and print each tuple, showing the item and its price in euros.
for i in store_euros:
    print(i)
