import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    print(word)
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print (f'You have {lives} ives left and you have used these letters: ', ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('letter is not in the word')
        elif user_letter in used_letter:
            print('You have already used that character. Please try again.')
        else: 
            print('Invalid character')
    if lives == 0:
        # print(lives_visual_dict[lives])
        print(f'You died, sorry. The word was {word}')
    else:
        print(f'YAY! You guessed the word {word}!!')

hangman()