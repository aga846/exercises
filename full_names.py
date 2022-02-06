

def extract_full_name(lst):
    lst2 = list([pair["first"], pair["last"]] for pair in lst)
    print([" ".join(x) for x in lst2])


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']


# ["Elie", "Schoppik"], ["Colt", "Steele"]
