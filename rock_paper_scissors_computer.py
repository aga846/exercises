from random import randint
import time

print("Rock...")
print("Paper...")
print("Scissors...\n")

player = input("Enter your choice: ").lower()
computer = randint(0, 2)

if computer == 0:
    computer = "rock"
elif computer == 1:
    computer = "paper"
elif computer == 2:
    computer = "scissors"

print(f"Computer choice: {computer}")
time.sleep(1)
if (player == "rock" and computer == "paper") or\
   (player == "paper" and computer == "scissors") or\
   (player == "scissors" and computer == "rock"):
    print("Computer wins!")
elif (player == "rock" and computer == "scissors") or\
     (player == "paper" and computer == "rock") or\
     (player == "scissors" and computer == "paper"):
    print("Player 1 wins!")
elif player == computer:
    print("It's a tie!")
else:
    print("Something went wrong :(")
