text = 'yesyes yowww'

with open(r'D:\UP Files\Python\Lesson\test.txt', 'w') as file:  #   it overwrites the txt file
    file.write(text)

with open(r'D:\UP Files\Python\Lesson\test.txt', 'a') as file:  #   it append on the text file
    file.write(text)

