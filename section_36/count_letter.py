def letter_counter(word):
    word = word.lower()

    def inner(letter):
        counter = word.count(letter)
        return counter

    return inner


lc = letter_counter("Amazing")
print(lc("a"))
