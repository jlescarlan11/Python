import time
import os

os.system('cls')

print("Loading in 5")
for n in range(4,0,-1):
    time.sleep(1)
    print(n)

time.sleep(1)


os.system('cls')


def stage_of_life(age):
    print("#######################\n\n\n")
    if age < 0:
        print("You have not been born yet!")
    elif 0 <= age <= 1:
        print("You are an infant.")
    elif 2 <= age <= 4:
        print("You are a toddler.")
    elif 5 <= age <= 12:
        print("You are a child.")
    elif 13 <= age <= 19:
        print("You are now a teen.")
    elif 20 <= age <= 39:
        print("You are now an adult.")
    else:
        print("You are now old.")
    print("\n\n\n\n#######################\n\n\n")

