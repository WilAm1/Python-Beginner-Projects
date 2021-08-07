"""Simple Hangman Game
a program that selects a random word 
and then allows the user to guess it in a game of hangman."""

word = 'hangman'
blank_word = "_"*len(word)
print('The word:  ',blank_word)
guess_letter = input("Guess the letter: ").lower()
blank_word_list = [i for i in blank_word]

if guess_letter in word:
    print("noice")
    for index, letter in enumerate(word):
        if letter == guess_letter:
            blank_word_list[index] = letter
            print(blank_word_list)
    blank_word = ''.join(blank_word_list)

            
            
    print(blank_word)