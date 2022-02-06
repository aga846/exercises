from csv import DictReader


def find_user(first, last):
    with open("names.csv") as file:
        csv_reader = DictReader(file)
        for index, x in enumerate(csv_reader):
            if x.get("First Name") == first and x.get("Last Name") == last:
                return index+1
        return "{} {} not found.".format(first, last)


print(find_user("Alan", "Turing"))
