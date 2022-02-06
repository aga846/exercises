stop = "stop copying me"
words = input("How are you?\n")

while words.lower() != stop:
    print(words)
    words = input()
