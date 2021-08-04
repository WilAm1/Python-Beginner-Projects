"""Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is."""

from random import randint



def game():
    rand_num = randint(1,100)
    guess = 0
    tries = 0
    print("Welcome to a Higher Lower Guessing Game! This is a simple game where you guess what number" \
        " the computer has!")
    while rand_num != guess:
        guess = int(input("Guess the number from 1 to 100 "))
        tries += 1

        if guess > rand_num:
            print("Lower!")
        elif guess < rand_num:
            print("Higher!")
        else:
            print(f"That's right! Congratulations! It took you {tries} tries!")
        
    if input('Do you want to play again? enter "yes" to continue  ') == 'yes':
        game()
    
    return

game()