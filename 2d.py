import random

number_1 = list(range(1, 32))
number_2 = list(range(1, 32))

specified_numbers = [16, 14, 10, 13, 6, 30]

number_1.extend(specified_numbers*3)
number_2.extend(specified_numbers*3)

with open('a.txt', 'a') as file:
    for i in range(1000):
        picked_number = [random.choice(number_1), random.choice(number_2)]
        file.write(f'{i+1}. {picked_number}\n')


