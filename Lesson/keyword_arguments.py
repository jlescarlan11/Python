"""
keyword arguments = arguments preceded by an identifier when we pass them to a function
                    The order of the arguments doesn't matter, unlike positional arguments
                    Python knows the names od the arguments that our function receives
"""

def hello(first, middle, last):
    print("Hello "+first+" "+middle+" "+last)

hello('Bro','Dude','Code') # This is what passing positional arguments is
hello(last='Code', middle='Dude', first='Bro') # This is what passing key arguments is
