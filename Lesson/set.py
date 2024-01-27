"""
set = collection which is unordered, unindexed. No duplicate values
"""

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'knife'}

# utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

print(utensils.difference(dishes)) # this print what utensils have that dishes haven't
print(utensils.intersection(dishes)) # this return what both have

# for x in dinner_table:
#     print(x)