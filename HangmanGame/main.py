"""Simple Hangman Game
a program that selects a random word 
and then allows the user to guess it in a game of hangman."""


from hangman_wordbank import HANGMANPICS, words 
from random import choice

LIVES = 6


def game(lives,word_list):
    """Run the main hangman game. """
    playing = True
    # Chooses a random word in the word_lists
    word = choice(word_list)
    
    blank_word = "_"*len(word)
    blank_word_list = [i for i in blank_word]
    # Loops until lives run out
    while playing:
        
        print(f"Lives : {lives}")
        print('The word:',  " ".join(blank_word_list))
        # Evaluate if it is valid to loop again
        if lives > 0 and '_' in blank_word_list:
            guess_letter = input("Guess the letter: ").lower()
            # Run if guessed letter is in the word
            if guess_letter in word:
                # Adds the letter to all same letter in  blank word 
                for index, letter in enumerate(word):
                    if letter == guess_letter:
                        blank_word_list[index] = letter
                        blank_word = ''.join(blank_word_list)
            # Prints the ASCII hangman if wrong answer
            else:
                lives -= 1
                print("you lose a life")
                print(HANGMANPICS[LIVES - lives])
        # Ends the game. Asks if user want to try again.
        else:
            playing = False
            if '_' in blank_word:
                print("You lose!")
            else:
                print("You win!")

            print(f"Game Over! The word is '{word}' !")

            play_again = input("Do you want to play again? type 'Yes' to continue  ").lower()
            if play_again == 'yes':
                game(LIVES)
        


welcome_text = "Welcome to hangman game! Guess a letter to complete the world!"
game(lives=LIVES,word_list=words)
