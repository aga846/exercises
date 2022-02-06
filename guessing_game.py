from random import randint

answer = "y"

while answer == "y":
    random_number = randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != random_number:
        if guess > random_number:
            guess = int(input("Too high, try again! "))
        elif guess < random_number:
            guess = int(input("Too low, try again! "))
    print("You guessed it! You won!")
    answer = input("Do you want to keep playing? (y/n) ")
