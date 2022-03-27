from random import randint

r1 = str(randint(0, 9))
r2 = str(randint(0, 9))
while r2 == r1:
    r2 = str(randint(0, 9))
r3 = str(randint(0, 9))
while r3 == r1 or r3 == r2:
    r3 = str(randint(0, 9))
code = r1 + r2 + r3

print("Code has been generated.")
guess = input("Your guess: ")
clues = []

while guess != code:
    if guess[0] == r1:
        clues.append("match")
    elif guess[0] in code:
        clues.append("close")
    if guess[1] == r2:
        clues.append("match")
    elif guess[1] in code:
        clues.append("close")
    if guess[2] == r3:
        clues.append("match")
    elif guess[2] in code:
        clues.append("close")
    if not clues:
        print("You haven't guess any of the numbers correctly.")
    else:
        print(f"Here are the clues: ", clues)
    clues = []
    guess = input("Your guess: ")

print("You guessed, congrats!")
