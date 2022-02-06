class Person:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"{self.first} is {self.age}"


damian = Person("Damian", "Jaskolski", 26)
aga = Person("Aga", "Jaskolski", 26)

aga = str(aga)
print(type(damian))
print(type(aga))
