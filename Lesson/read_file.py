

try:
    with open(r'D:\UP Files\Python\Lesson\test.txt') as file:   #   You can write any names alternative to file
        print(file.read())
except FileNotFoundError:
    print("That file is not found")
else:
    print(file.closed)  #   This check if the file has been closed