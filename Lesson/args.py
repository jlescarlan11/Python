"""
*args = parameter that will pack all arguments into a tuple
        useful so that a function can accept a varying amount of arguments
"""

def add(*args): # the parameter args is not important, the asterisk is
                # you can change the name args to any variable name
    sum = 0
    # args[0] = 0 # this will result into an error
    args = list(args)   # args is unchangeable like any tuple
                        # to make it changeable, try to convert it first into the list
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3))