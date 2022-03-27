def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return num


print(fizz_buzz(15))
print(fizz_buzz(9))
print(fizz_buzz(20))
print(fizz_buzz(4))
