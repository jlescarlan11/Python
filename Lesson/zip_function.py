"""
zip(*iterables) =   aggregate elements from two or more iterables (lists, tuples, sets, etc.)
                    create a zip object with paired elements stored in tuples for each corresponding element

Learned: Creating a dictionary using zip to pair elements from two lists and create key-value pairs.
"""

# You can add another variable here, not just 2
usernames = ['Dude', 'Bro', 'Mister']
passwords = ['p@ssword', 'abc123', 'guest']

# Creating a dictionary using zip
users = dict(zip(usernames, passwords))

print(type(users))

# Displaying the key-value pairs in the dictionary
for key, value in users.items():
    print(key + " : " + value)
