"""Write a function that prints all the prime numbers between 0 and limit where limit is a parameter."""


def prime(limit):
    for i in range(2, limit+1):
        flag = True
        for j in range(2, i//2+1):
            if i % j == 0:
                flag = False
                break
            else:
                pass
        if flag == True:
            print(i)


prime(15)
