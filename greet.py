def be_polite(y):
    def wrapper():
        print("hey")
        y()
        print("bye")
    return wrapper


def greet(name):
    print(f"name: {name}")


x = be_polite(greet("Damian"))
x()
