import random
import os

def random_number():
    return random.randint(30, 67)

number = random_number()

os.system('cls')

with open('30_days_hulog.txt', 'a') as file:
    file.write(f'{number}')

print(f"\n\n\n\nMaghulog ka ng {number} pesos\n\n\n")