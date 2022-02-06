print("Rock...")
print("Paper...")
print("Scissors...\n")

player1 = input("Enter Player 1's choice: ").lower()
print("NO CHEATING!\n" * 50)
player2 = input("Enter Player 2's choice: ").lower()

if (player1 == "rock" and player2 == "paper") or\
   (player1 == "paper" and player2 == "scissors") or\
   (player1 == "scissors" and player2 == "rock"):
    print("Player 2 wins!")
elif (player1 == "rock" and player2 == "scissors") or\
     (player1 == "paper" and player2 == "rock") or\
     (player1 == "scissors" and player2 == "paper"):
    print("Player 1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went wrong :(")
