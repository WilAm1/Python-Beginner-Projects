"""Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is."""

from random import randint

rand_num = randint(1,100)

guess = input("Guess the number from 1 to 100")

if guess > rand_num:
    print("Lower!")
elif guess < rand_num:
    print("Higher")
else:
    print("That's right! Congratulations!")

