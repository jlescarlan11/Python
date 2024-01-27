import os

source = 'test.txt'
destination = r'D:\UP Files\Python\Lesson\test.txt'

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(f"{source} was moved") 
except FileNotFoundError:
    print(f"{source} was not found")