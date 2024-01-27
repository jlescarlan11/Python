"""
list = used to store multiple items in a single variable
"""

food = ['pizza', 'hamburgers', 'hotdog', 'spaghetti']

food[0] = 'sushi' 

food.append("ice cream") # add an element to the list
food.remove("hamburgers") # remove a value in the list
food.pop(-2) # remove the last element, but you can assign an index where to remove
food.insert(0, 'cake') # add a value in the given index
food.sort() # sort the list alphabetically
food.clear() # clears all the elements in the list.

# print(food[1])
# for _ in food:
#     print("\t- "+ _)