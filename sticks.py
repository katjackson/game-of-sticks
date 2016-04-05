import random
from os import system

def clear():
    system('clear')

def adjust_rem_sticks(rem_sticks, guess):
    return rem_sticks - guess


def get_max_guess(rem_sticks):
    max_guess = 3
    if rem_sticks < 3:
        max_guess = rem_sticks
    return max_guess


def get_guess_from_input(player, max_guess):
    guess = input("How many sticks do you take, {}? (1 - {}) ".format(player, max_guess))
    if is_valid_number(guess, max_guess):
        return int(guess)
    else:
        return get_guess_from_input(player, max_guess)


def get_player_names_from_input():
    player_1 = input("\nPlayer 1, what is your name? ")
    player_2 = input("\nPlayer 2, what is your name? ")
    return player_1, player_2


def print_board(rem_sticks):
    print('\n')
    print("There are {} sticks on the board.".format(rem_sticks))
    return("There are {} sticks on the board.".format(rem_sticks))


def is_loser(rem_sticks):
    return rem_sticks == 0


def is_valid_number(number, max_number, min_number = 0):
    try:
        if min_number < int(number) <= max_number:
            return True
        else:
            raise Exception
    except:
        print("Please choose a number from {} to {}.".format(min_number, max_number))
        return False


def get_rem_sticks_from_input():
    rem_sticks = input("How many sticks should we play with? (10 - 100) ")

    if is_valid_number(rem_sticks, 100, 10):
        return int(rem_sticks)
    else:
        return get_rem_sticks_from_input()



def main():

    clear()
    print("\nWelcome to the Game of Sticks!\n")

    player_1, player_2 = get_player_names_from_input()
    print('\n')
    rem_sticks = get_rem_sticks_from_input()

    clear()
    while rem_sticks > 0:

        for player in [player_1, player_2]:

            print_board(rem_sticks)
            guess = get_guess_from_input(player, get_max_guess(rem_sticks))
            rem_sticks = adjust_rem_sticks(rem_sticks, guess)

            if is_loser(rem_sticks):
                print("You lose!")
                if input("Do you want to play again? y/N ").lower() == 'y':
                    return main()

            clear()


if __name__ == '__main__':
    main()
