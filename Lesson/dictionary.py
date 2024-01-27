"""
dictionary =    A changeable, unordered collection of unique key: value pairs
                Fast because they use hasing, allow us to access a value quickly
"""

capitals = {
    'USA' : 'Washington DC',
    'India' : 'New Dehli',
    'China' : 'Beijing',
    'Russia' : 'Moscow'
    }

# print(capitals['Russia'])   # This may get an error if we try to get the 
#                             # capital of germany
# print(capitals.get('Russia'))   # This is much safer way if we want to 
#                                 # check if the key we want to find is 
#                                 # in  dictionary
# print(capitals.keys()) # This will only print the keys in the dictionary
# print(capitals.values()) # This will only print the values in the dictonary
# print(capitals.items()) # This will print the entire dictionary
# capitals.update({'Germany':'Berlin'}) # Add new key:value pair
# capitals.update({'USA':'Las Vegas'}) # Also, it can update the value of the key
# capitals.pop('China') # This remove a key value pair
# capitals.clear() # This removes everything

for key,value in capitals.items():
    print(key + " : " + value)

