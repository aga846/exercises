"""If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit(70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
"""


def drivers_speed(speed):
    if speed <= 70:
        return "Ok"
    else:
        points = (speed-70)/5
        if points > 12:
            return "License suspended"
        else:
            return f"Points: {int(points)}"


print(drivers_speed(65))
print(drivers_speed(74))
print(drivers_speed(240))
