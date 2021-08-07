"""Simple Hangman Game
a program that selects a random word 
and then allows the user to guess it in a game of hangman."""

word = 'hangman'
blank_word = "_"*len(word)
print('The word:  ',blank_word)

blank_word_list = [i for i in blank_word]
lives = 5
playing = True

while playing:
    guess_letter = input("Guess the letter: ").lower()
    if lives > 0 and '_' in blank_word:
        if guess_letter in word:
            for index, letter in enumerate(word):
                if letter == guess_letter:
                    blank_word_list[index] = letter
                    print(blank_word_list)
        else:
            lives -= 1
            print("you lose a life")
    else:
        print("Game Over")
        playing = False
    
    blank_word = ''.join(blank_word_list)

            
            
    print(blank_word)
    print(f"You only have {lives} lives")