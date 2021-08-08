"""Simple Hangman Game
a program that selects a random word 
and then allows the user to guess it in a game of hangman."""


from hangman_wordbank import HANGMANPICS, words 
from random import choice



def game(lives):
    playing = True
    word = choice(words)
    blank_word = "_"*len(word)
    blank_word_list = [i for i in blank_word]
    while playing:

        
        print(f"Lives : {lives}")
        print('The word:',  " ".join(blank_word_list))
        if lives > 0 and '_' in blank_word_list:
            guess_letter = input("Guess the letter: ").lower()
            if guess_letter in word:

                for index, letter in enumerate(word):

                    if letter == guess_letter:
                        blank_word_list[index] = letter
                        blank_word = ''.join(blank_word_list)
            else:
                lives -= 1
                print("you lose a life")
                print(HANGMANPICS[LIVES - lives])
        else:
            playing = False
            if '_' in blank_word:
                print("You lose!")
            else:
                print("You win!")

            print(f"Game Over! The word is {word}")
            play_again = input("Do you want to play again? type 'Yes' to continue  ").lower()
            if play_again == 'yes':
                game(LIVES)
        

welcome_text = "Welcome to hangman game! Guess a letter to complete the world!"

LIVES = 6

game(lives=LIVES)
