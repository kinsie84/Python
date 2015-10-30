__author__ = 'Peter Kinsella'


import random


filename = 'dictionary.txt'                             # import external file
random_words = []
with open ( filename , "r" ) as f :
    for currentword in f :
        currentword = currentword [: -1]
        if len(currentword) > 4:                       # Specify min length of word from file
            random_words.append(currentword)


guessed_letters = []                                    # Global Variable used to hold guessed letters
word = random.choice(random_words)                      # Global Variable used to generate random word
blanks = '_' * len(word)                                # Global Variable used to generate underscores in place of word letters
guessed_word = list(blanks)                             # Global Variable used to convert blanks into a list


def check_guess(word):                                  # Function checks if guess is in word
    turn = 10                                           # Holds number of turns for the game
    while check_word(guessed_word) is False:            # Checks check_word() function to see if word has been guessed
        print(guessed_word)
        print("You have",turn,"attempts remaining")
        guess = str.lower(input("Enter a single alphabetical guess:"))              # Asks user for input and converts to lower case
        if guess_control(guess) is False:               # Checks guess_control function to ensure criteria are met
            continue
        elif guess in word:
            guessed_letters.append(guess)               # Appends guess to guessed_letters list
            update_guessed_word(guess)                  # Runs update_guessed_word function to add correct guess
        elif guess not in word:
            print("Incorrect guess")
            guessed_letters.append(guess)               # Appends guess to guessed_letters list
            turn -= 1                                   # Reduces turns by 1
            if turn == 0:                               # Checks if no turns are left
                print("You lose! \nThe correct word was:",word)
                break


def guess_control(guess):                               # Function checks if guess meets 3 criteria of an allowed guess
    if len(guess) > 1:
        print("You can only guess one letter at a time, \nTry again")
        return False
    elif str.isalpha(guess) is False:
        print("Guess must be alphabetical \nTry again")
        return False
    elif guess in guessed_letters:
        print("You've already guessed that \nTry again")
        return False


def update_guessed_word(guess):                         # Function adds guessed letters to all places in the word it appears
    for letter in range(len(word)):
        if guess == word[letter]:
            guessed_word[letter] = guess


def check_word(guessed_word):                           # Function checks total correct guesses to see if it matches the word
    if ''.join(guessed_word) == word:                   # Converts guessed_word list into a word and checks if it matches the word
        print("You guessed it  ---> ",word,"\nYou Win!")
        return True
    else:
        return False


def main():
    print("Word is of length:",len(word))
    check_guess(word)


main()
