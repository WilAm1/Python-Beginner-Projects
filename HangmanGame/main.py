"""Simple Hangman Game
a program that selects a random word 
and then allows the user to guess it in a game of hangman."""



word = 'hangman'
blank_word = "_"*len(word)


blank_word_list = [i for i in blank_word]
lives = 5
playing = True

welcome_text = "Welcome to hangman game! Guess a letter to complete the world!"
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
            print(f"You only have {lives} lives")
    else:
        if '_' in blank_word:
            print("You lose!")
        else:
            print("You win!")

        print("Game Over")
        playing = False
    
    

    