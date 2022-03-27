def next_prime():
    i = 2
    while True:
        prime = True
        if i > 3:
            for d in range(2, int(i/2)+1):
                print(f"For loop for {d}")
                if i % d == 0:
                    print(f"{i} % {d} equals 0")
                    prime = False
                    break
        if prime is True:
            yield i
        i += 1


p = next_prime()
print(next(p))
print(next(p))
print(next(p))
