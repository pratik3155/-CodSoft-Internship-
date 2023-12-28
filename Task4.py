'''
Task 4
Rock-Paper-Scissors Game
'''

import random
import math

def play():
    user = input("What's your choice? 'r' for Rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 0, user, computer

    if is_win(user, computer):
        return 1, user, computer

    return -1, user, computer

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_again():
    answer = input("Do you want to play again? (yes/no)\n").lower()
    return answer == 'yes'

def play_best_of(n):
    while True:
        player_wins = 0
        computer_wins = 0
        wins_necessary = math.ceil(n / 2)
        print(wins_necessary)

        while player_wins < wins_necessary and computer_wins < wins_necessary:
            result, user, computer = play()

            if result == 0:
                print("It's a Tie. You and the computer have both chosen {}.\n".format(user))
            elif result == 1:
                player_wins += 1
                print("You chose {} and the computer chose {}. You Won.\n".format(user, computer))
            else:
                computer_wins += 1
                print("You chose {} and the computer chose {}. You lost.\n".format(user, computer))
            print("\n")

        if player_wins > computer_wins:
            print("You have won the best of {} games! What a champ :D".format(n))
        else:
            print("Unfortunately, the computer has won the best of {} games. Better luck next time.".format(n))

        if not play_again():
            break

if __name__ == '__main__':
    play_best_of(3)
