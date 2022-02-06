#for i in range(1, 11):
#    print("\U0001f600" * i)

#i = 1
#while i < 11:
#    print("\U0001f600" * i)
#    i += 1
print(" " * 9)
for i in range(1, 8, 2):
    spaces = 9-i
    print((" " * spaces) + ("\U0001f600" * i) + (" " * spaces))
print("\U0001f600" * 9)
