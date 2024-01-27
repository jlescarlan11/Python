"""
**kwargs =  parameter that will pack all arguments into a dictionary
            useful so that a function can accept a varying amount of keyword argument
"""

def hello(**kwargs):    # the parameter name kwargs is not important here, the asterisk is
    print('Hello ' + kwargs['first'] + " " + kwargs['last'])
    print('Hello', end=' ')
    for key, value in kwargs.items():
        print(value.title(), end=' ')
    

hello(title='mr.', first = 'bro', middle='dude', last = 'code')
