"""
function = a block of code which is executed only when it is called.
"""

def hello(first_name, last_name, age=21): # the inside of the parenthesis here is called the parameter
    print("Hello "+first_name.title()+' '+last_name.title())
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

my_first_name = 'lest'
my_last_name = 'code'
hello('lest', 'code', 19) # the inside of the parenthesis here is called an arguments
# hello(my_first_name, my_last_name) # this is also possible to be argument