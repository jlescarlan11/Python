import random
import os
import time

def clear_console():
    os.system('cls')

def get_player_name():
    player_name = ''
    while not player_name:
        player_name = input('\nEnter your name: ').title()
        sure_name = False
        while not sure_name:
            ask_if_sure = input('Are you sure? (yes/no) ').lower()
            if ask_if_sure == 'yes':
                sure_name = True
            elif ask_if_sure == 'no':
                player_name = ''
                break
            else:
                print('Invalid input. Please enter yes or no.')
        clear_console()
    return player_name

def print_outcome(player_name, player, computer, outcome):
    print(f'Computer: {computer}')
    print(f'{player_name}: {player}')
    print(outcome)

def determine_winner(player, computer, player_name, player_score, computer_score):
    if player == computer:
        print_outcome(player_name, player, computer, 'Tie!')
    elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
        player_score += 1
        print_outcome(player_name, player, computer, f'{player_name} wins!')
    elif (player == 'paper' and computer == 'scissors') or (player == 'scissors' and computer == 'rock') or (player == 'rock' and computer == 'paper'):
        computer_score += 1
        print_outcome(player_name, player, computer, 'Computer wins!')
    
    return player_score, computer_score

    

def print_scores(player_name, player_score, computer_score):
    print(f'\n\n##################<Scores>##################')
    print(f'{player_name}: {player_score}\nComputer: {computer_score}')
    print(f'############################################')


def play_game():
    player_score = 0
    computer_score = 0
    winning_score = 3

    player_name = get_player_name()

    print(f'Hello, {player_name}. Thank you for playing this game.')
    time.sleep(3)
    clear_console()
    print('The rule is simple, defeat your computer in rock, paper, and scissors!')
    time.sleep(3)
    clear_console()
    input('Now, click enter to continue, and smash that computer! ')
    clear_console()
    
    while (player_score < winning_score) and (computer_score < winning_score):
        choices = ['rock', 'paper', 'scissors']

        computer = random.choice(choices)
        player = ''

        while player not in choices:
            print_scores(player_name, player_score, computer_score)
            player = input('\n\nEnter your choice (rock, paper, scissors): ').lower().strip()
            clear_console()

        player_score, computer_score = determine_winner(player, computer, player_name, player_score, computer_score)

        print_scores(player_name, player_score, computer_score)

        input('\n\nClick enter to continue! ')
        clear_console()

    if computer_score == winning_score:
        another_round = input("Computer wins! Do you want to get your revenge? (yes/no) ").lower().strip()
        while another_round not in ['yes', 'no']:
            print('Enter yes or no only!')
            another_round = input("Do you want to play another round? (yes/no)").lower().strip()

        if another_round == 'no':
            return False  # Return False to indicate not playing again
    else:
        another_round = input(f"{player_name} wins! Do you want to humiliate this computer again? (yes/no) ").lower().strip()
        while another_round not in ['yes', 'no']:
            print('Enter yes or no only!')
            another_round = input("Do you want to play another round? (yes/no)").lower().strip()

        if another_round == 'no':
            return False  # Return False to indicate not playing again

    return True  # Return True to indicate playing again

clear_console()


while True:
    if not play_game():
        break








