"""Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
*****
"""


def show_stars(rows):
    stars = ""
    for i in range(1, rows+1):
        if i < rows:
            stars += "*" * i + "\n"
        else:
            stars += "*" * i
    return stars


print(show_stars(5))
