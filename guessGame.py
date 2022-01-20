# ------- MIMIC GAME / INTERACTIONS BETWEEN FUNCTIONS

from random import shuffle

example = [1, 2, 3, 4, 5, 6]


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(example)
print(result)
mylist = [' ', 'O', ' ']
print(shuffle_list(mylist))


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0,1, or 2')
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print('mylist')


# INITIAL LIST
mylist = [' ', 'O', ' ']
# SHUFFLE LIST
mixed_up_list = shuffle_list(mylist)
# USER GUESS
guess = player_guess()
# CHECK GUESS
check_guess(mixed_up_list, guess)
