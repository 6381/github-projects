import random

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''']

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']


def play_hangman():
    word = random.choice(words)
    guessed_letters = ['_'] * len(word)
    missed_letters = ''
    max_misses = 6

    while True:
        print(HANGMAN_PICS[len(missed_letters)])
        print(' '.join(guessed_letters))
        print('Missed letters:', missed_letters)

        guess = input('Guess a letter: ').lower()

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_letters[i] = guess
        else:
            missed_letters += guess
            max_misses -= 1

        if '_' not in guessed_letters:
            print('Congratulations! You won!')
            break
        elif max_misses == 0:
            print('Sorry, you lost! The word was', word)
            break


play_hangman()