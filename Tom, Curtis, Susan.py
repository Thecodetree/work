import random

import math

def play():

    user = input("What is your choice? 't' for tom, 's' for susan, 'c' for curtis\n")
    user = user.lower()

    computer = random.choice(['t', 's', 'c'])

    if user == computer:
        return (0, user, computer)
    
    if is_win(user, computer):
        return (1, user, computer)

        return (-1, user, computer)

    def is_win(player, opponent):

        if (player == 't' and opponent == 's') or (player == 's' and opponent == 'c') or (player == 'c' and opponent == 't'):
            return True
    return False
       

def play_best_of(n):
    Player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while Player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()

        if result == 0:
            print('This is diappointing. You have tied You and the computer have both chosen {}. \n'.format(user))
        elif result == 1:
            Player_wins += 1
            print('You chose {} and computer chose {}. You are the mighty one!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('you chose {} and the computer chose {}. You have failed the family name!: \n'.format(user, computer))
        print('\n')

        if Player_wins > computer_wins:
            print('You have won best of {} games! Now you shall reign as king!')
        else:
            print('Unfortunately the computer has won best of {} games. You have been failed for the last time!')      

if __name__ == '__main__':
    play_best_of(3)
    play_best_of(9)

