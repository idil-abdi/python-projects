########### Dice Rolling Game ###########

###### MY ATTEMPT: ######
# choice = input('Roll the dice? (y/n): ')
# if choice == 'y':
#     print('Lets Start.')
# elif choice == 'n':
#     print('Thank you for playing!')
# else:
#     print('Invalid Choice!')

###### SOLUTION: ######   TIPS - psudocode you answer
#                                - loop
#                                -   Ask: roll the dice?
#                                -   if user enters y
#                                -     generate two random numbers
#                                -     print them
#                                -   if user enters n
#                                -     print thank you message
#                                -     terminate
#                              - too keep asking until user terminate we put it in a loop
#                              - import random if you need any random number
#                              - while loop is an endless loop until break
import random

while True: 
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        print(f'({dice_1}, {dice_2})')
    elif choice == 'n':
        print('Thank you for playing!')
        break
    else:
        print('Invalid Choice!')