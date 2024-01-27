"""
str.format() =  optional method that gives users more control when displaying output
"""

############################################################################
animal = 'cow'
item = 'moon'

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {1} jumped over the {0}".format(item,animal))    #   positional argument
# print("The {animal} jumped over the {item}".format(animal='cow',item='moon'))   #   keyword arguments
# print(f"The {animal:10} jump over the {item}") 

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

#############################################################################
name =  'Bro'

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))    # Left alligning the format name
# print("Hello, my name is {:>10}. Nice to meet you".format(name))    #   Right alligning the format name
# print("Hello, my name is {:^10}. Nice to meet you".format(name))    #   Center alligning the format 

##############################################################################

number = 1000

print(f"The number is {number:.2f}") # if want to show n decimal number
print(f"The number is {number:,}")   #   add comma after thousand place
print(f"The number is {number:b}")   #   display binary representation
print(f"The number is {number:o}")   #   display octal representation
print(f"The number is {number:X}")  #   display hexadecimal, lowercase x for lowercase, uppercase X for uppercase
print(f"The number is {number:e}")  #   display in scientific notation 



