import random

dice = random.randint(1,6)


myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)   #   This pick a random choice

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)   #   This shuffles the list

print(cards)