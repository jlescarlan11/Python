"""
1. Module can be run as a standalone program
    or
2. Module can be imported and used by other modules

Python interpreter sets "special variables", one of which is __name.
Python will assign the __name__ variable a value of '__main__' if it's
the initial module being run.

In this code, the 'if __name__ == '__main__':' condition checks whether
this script is being run as the main program. If it is, the 'main()' 
function is called, allowing modular use of the script without executing
the 'main()' function if the script is imported as a module in another program.
"""



def main():
    print('Hello!')

# # Check if the script is being run as the main program
if __name__ == '__main__':
    main()  # Execute the main function if this script is the entry point
    
# main()

    
