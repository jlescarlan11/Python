"""
scope = The region that a variable is recognized
        A variable is only available from inside the region it is created.
        A global and locally scoped versions of a variable that can be created
"""

name = 'Bro'    #   global scope    (available inside & outside function)
def display_name():
    name = 'Code'   #   local scope (available only inside this function)
    print(name)

display_name()
print(name)