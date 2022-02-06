from csv import reader


def find_user(first, last):
    with open("names.csv") as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader):
            first_match = first == row[0]
            last_match = last == row[1]
            if first_match and last_match:
                return index
        return "{} {} not found.".format(first, last)


print(find_user("Colt", "Steele"))
