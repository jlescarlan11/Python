"""
while loops = a statement that will execute its block of code, 
                as long as its condition remains true
"""

# # This is infinite loop
# while 1==1:
#     print("Help sis, I'm stuck!")

name = ''

while not name:
    name = input("Enter your name: ")

print("Hello, "+name)
