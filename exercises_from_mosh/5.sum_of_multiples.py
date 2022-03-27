"""Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20."""


def sum_of_mltp(limit):
    s = 0
    for i in range(0, limit+1, 3):
        s += i
    for i in range(0, limit+1, 5):
        s += i
    return s


print(sum_of_mltp(10))
