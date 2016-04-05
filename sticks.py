import random
import copy
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


def get_version():
    if input("What version do you want to play?\n1. 2-Player\n2. Player v Computer\n") == '1':
        return '1'
    else:
        return '2'


def play_version_1():

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
                break

            clear()


def make_a_guess(rem_sticks, dict_of_hats):
    return random.choice(dict_of_hats[rem_sticks])

def add_guess_to_hat(guess, rem_sticks, dict_of_hats):
    dict_of_hats[rem_sticks].append(guess)
    return dict_of_hats


def print_check_dict(a_dict):
    print(a_dict[1])
    print(a_dict[2])
    print(a_dict[3])
    print(a_dict[4])
    print(a_dict[5])
    print(a_dict[6])
    print(a_dict[7])
    print(a_dict[8])
    print(a_dict[9])
    print(a_dict[10])
    print(a_dict[11])

def play_version_2(starting_dict_of_hats):

    player_1 = input("\nPlayer 1, what is your name? ")
    # player_2 = 'AI'

    print('\n')
    rem_sticks = get_rem_sticks_from_input()
    working_dict_of_hats = copy.deepcopy(starting_dict_of_hats)

    print_check_dict(starting_dict_of_hats)
    print_check_dict(working_dict_of_hats)

    clear()
    while rem_sticks > 0:


        # player_1 turn
        print_board(rem_sticks)
        guess = get_guess_from_input(player_1, get_max_guess(rem_sticks))
        rem_sticks = adjust_rem_sticks(rem_sticks, guess)

        if is_loser(rem_sticks):
            print("You lose!")
            return working_dict_of_hats


        # player_2 turn
        print_board(rem_sticks)
        guess = make_a_guess(rem_sticks, working_dict_of_hats)
        working_dict_of_hats = add_guess_to_hat(guess, rem_sticks, working_dict_of_hats)
        print("AI picks up {} sticks.".format(guess))
        rem_sticks = adjust_rem_sticks(rem_sticks, guess)

        if is_loser(rem_sticks):
            print("You win!")
            return starting_dict_of_hats
            break

        print_check_dict(starting_dict_of_hats)
        print_check_dict(working_dict_of_hats)

starting_dict_of_hats = {key: [1, 2, 3] for key in range(1, 101)}
starting_dict_of_hats[1] = [1]
starting_dict_of_hats[2] = [1, 2]

def main(starting_dict_of_hats):


    clear()
    print("\nWelcome to the Game of Sticks!\n")

    version = get_version()

    if version == '1':
        play_version_1()

    if version == '2':
        starting_dict_of_hats = play_version_2(starting_dict_of_hats)

    print_check_dict(starting_dict_of_hats)

    if input("Do you want to play again? y/N ").lower() == 'y':
        return main(starting_dict_of_hats)
    else:
        print('Goodbye')



if __name__ == '__main__':
    main(starting_dict_of_hats)




# p2 computer option
