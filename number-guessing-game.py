########### Number Guessing Game ###########

###### MY ATTEMPT: ######
"""
psudocode:
            ask user to guess a number from 1 to 100 ✔️
            generate a random num ✔️
            if user num equl to random num
                print congratulation number
                terminate
            if user num is greater then random num
                print too high
                continue the game
            if user num is less then random num
                print too low
                continue the game
            if user num is not within range 
                print please a valid num
                continue the game
"""

"""
import random

user_num = input('Guess a number from 1 to 100: ')
random_num = random.random()

while True:
    if 1 <= user_num and user_num <= 100:
        if user_num == random_num:
            print('Congratulation! You guessed the number.')
            break
        elif user_num > random_num:
            print('Too High!')
        elif user_num < random_num:
            print('Too Low!')
    else:
        print('Please a valid number')
"""

###### SOLUTION: ######   TIPS - psudocode you answer
#                                - generate a random num
#                                - loop
#                                -   ask user to guess a number from 1 to 100
#                                -     if user num is not a valid num
#                                -       print error
#                                -     if user num is greater then guess
#                                -       print too high
#                                -     if user num is lower then guess
#                                -       print too low
#                                -     else
#                                -       well done

import random

num_to_guess =random.randint(1,100)

while True:
    try:
        user_guess = int(input('Guess a number from 1 to 100: '))
        if user_guess < num_to_guess:
            print('Too Low')
        elif user_guess > num_to_guess:
            print('Too High!')
        else:
            print('Congratulation! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')

